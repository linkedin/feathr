
from typing import Union
from uuid import UUID
from azure.identity import DefaultAzureCredential
from pyapacheatlas.auth.azcredential import AzCredentialWrapper
from pyapacheatlas.core import (AtlasEntity, AtlasProcess,AtlasException,
                                PurviewClient)
from pyapacheatlas.core.util import GuidTracker

Label_Contains = "CONTAINS"
Label_BelongsTo = "BELONGSTO"
Label_Consumes = "CONSUMES"
Label_Produces = "PRODUCES"
guid = GuidTracker(starting=-1000)

def _generate_relation_pairs(from_entity, to_entity, relation_type):
    global guid
    type_lookup = {Label_Contains: Label_BelongsTo, Label_Consumes: Label_Produces}
    forward_relation =  AtlasProcess(
        name=str(from_entity["guid"]) + " to " + str(to_entity["guid"]),
        typeName="Process",
        qualified_name='__'.join(
            [relation_type,str(from_entity["guid"]), str(to_entity["guid"])]),
        inputs=[from_entity],
        outputs=[to_entity],
        guid=guid.get_guid())
    
    backward_relation = AtlasProcess(
        name=str(to_entity["guid"]) + " to " + str(from_entity["guid"]),
        typeName="Process",
        qualified_name='__'.join(
            [type_lookup[relation_type], str(to_entity["guid"]), str(from_entity["guid"])]),
        inputs=[to_entity],
        outputs=[from_entity],
        guid=guid.get_guid())
    return [forward_relation,backward_relation]
def upload_single_entity_to_purview(purview_client,entity:Union[AtlasEntity,AtlasProcess]):
    try:
        entity.lastModifiedTS="0"
        result = purview_client.upload_entities([entity])
        entity.guid = result['guidAssignments'][entity.guid]
        print(f"Successfully created {entity.typeName} -- {entity.qualifiedName}")
    except AtlasException as e:
        if "PreConditionCheckFailed" in e.args[0]:
            entity.guid = purview_client.get_entity(qualifiedName=entity.qualifiedName,typeName = entity.typeName)['entities'][0]['guid']
            print(f"Found existing entity  {entity.guid}, {entity.typeName} -- {entity.qualifiedName}")
    return UUID(entity.guid)
default_purview_name = "feathrazuretest3-purview1"   
default_project_name = "feathr_ci_registry_35_47_50416"                            
credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
oauth = AzCredentialWrapper(credential=credential)
purview_client = PurviewClient(
    account_name=default_purview_name,
    authentication=oauth)

project_search_term = {"entityType": "feathr_workspace_v1"}
result = purview_client.discovery.query(filter=project_search_term)
project_entities = [x for x in result['value']]


for entity in project_entities:
    project_entity = purview_client.get_entity(entity["id"])['entities'][0]
    entities_in_project = []
    query_filter = {
        "and": [
            {
                "or":
                [
                    {"entityType": "feathr_anchor_v1"},
                    {"entityType": "feathr_source_v1"},
                    {"entityType": "feathr_anchor_feature_v1"},
                    {"entityType": "feathr_derived_feature_v1"}
                ]
            },
            {
                "attributeName": "qualifiedName",
                "operator": "startswith",
                "attributeValue": project_entity['attributes']['qualifiedName'] + "__"
            }
        ]
    }
    entities_in_project = purview_client.discovery.query(filter=query_filter)['value']     
               
    anchors = [x for x in entities_in_project if x['entityType']=='feathr_anchor_v1']
    sources = [x for x in entities_in_project if x['entityType']=='feathr_source_v1']
    anchor_features = [x for x in entities_in_project if x['entityType']=='feathr_anchor_feature_v1']
    derived_features = [x for x in entities_in_project if x['entityType']=='feathr_derived_feature_v1']

    for source in sources:
        source_entity = purview_client.get_entity(source['id'])['entities'][0]
        relations = _generate_relation_pairs(project_entity,source_entity,Label_Contains)
        [upload_single_entity_to_purview(purview_client,x) for x in relations]
    for anchor in anchors:
        anchor_entity = purview_client.get_entity(anchor['id'])['entities'][0]
        source_entity = None
        relations=[]
        relations+= _generate_relation_pairs(project_entity,anchor_entity,Label_Contains)
        if anchor_entity['attributes']['source']:
            source_entity = purview_client.get_entity(anchor_entity['attributes']['source']['guid'])['entities'][0]
            relations+= _generate_relation_pairs(anchor_entity,source_entity,Label_Consumes)

        containing_anchor_features = [x for x in anchor_features if x['qualifiedName'].startswith(project_entity['attributes']['qualifiedName'] + "__"+anchor['name'])]
        for containing_anchor_feature in containing_anchor_features:
            anchor_feature_entity = purview_client.get_entity(containing_anchor_feature['id'])['entities'][0]
            relations+= _generate_relation_pairs(project_entity,anchor_feature_entity,Label_Contains)
            if source_entity:
                relations+= _generate_relation_pairs(anchor_feature_entity,source_entity,Label_Consumes)
        [upload_single_entity_to_purview(purview_client,x) for x in relations]
    for derived_feature in derived_features:
        derived_feature_entity = purview_client.get_entity(derived_feature['id'])['entities'][0]
        input_feature_entities = []
        relations=[]
        relations+=_generate_relation_pairs(project_entity,derived_feature_entity,Label_Contains)

        if 'input_derived_features' in derived_feature_entity['attributes'] or 'input_anchor_features' in derived_feature_entity['attributes']:
            input_features = [x['guid'] for x in derived_feature_entity['attributes']['input_derived_features']+derived_feature_entity['attributes']['input_anchor_features']]
            input_feature_entities = [purview_client.get_entity(x)['entities'][0] for x in input_features]
        for input_Feature_entity in input_feature_entities:
            relations+=_generate_relation_pairs(derived_feature_entity,input_Feature_entity,Label_Consumes)
        [upload_single_entity_to_purview(purview_client,x) for x in relations]

    
