
from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Optional

from jinja2 import Template
import json


class SourceSchema(ABC):
    pass


class AvroJsonSchema(SourceSchema):
    """Avro schema written in Json"""
    def __init__(self, schemaStr:str):
        self.schemaStr = schemaStr

    def to_feature_config(self):
        tm = Template("""
        schema: {
            type = "avro"
            avroJson:{{avroJson}}
        }
        """)
        avroJson = json.dumps(self.schemaStr)
        msg = tm.render(schema=self, avroJson=avroJson)
        return msg


class Source:
    """External data source for feature. Typically a 'table'.
     Attributes:
         name: name of the source
         event_timestamp_column: column name of the event timestamp
         timestamp_format: the format of the event_timestamp_column, e.g. yyyy/MM/DD.
         registry_tags: A dict of (str, str) that you can pass to feature registry for better organization. For example, you can use {"deprecated": "true"} to indicate this source is deprecated, etc.
    """
    def __init__(self,
                 name: str,
                 event_timestamp_column: Optional[str] = "0",
                 timestamp_format: Optional[str] = "epoch",
                 registry_tags: Optional[Dict[str, str]] = None,
                 ) -> None:
        self.name = name
        self.event_timestamp_column = event_timestamp_column
        self.timestamp_format = timestamp_format
        self.registry_tags = registry_tags

    def __eq__(self, other):
        """A source is equal to another if name is equal."""
        return self.name == other.name

    def __hash__(self):
        """A source can be identified with the name"""
        return hash(self.name)

    def to_write_config(self) -> str:
        pass

    def __str__(self):
        return self.to_feature_config()


class InputContext(Source):
    """A type of 'passthrough' source, a.k.a. request feature source.
    """
    SOURCE_NAME = "PASSTHROUGH"
    def __init__(self) -> None:
        super().__init__(self.SOURCE_NAME, None, None)

    def to_feature_config(self) -> str:
        return "source: " + self.name


class HdfsSource(Source):
    """A data source(table) stored on HDFS-like file system. Data can be fetch through a POSIX style path.

        Args:
            name (str): name of the source
            path (str): The location of the source data.
            preprocessing (Optional[Callable]): A preprocessing python function that transforms the source data for further feature transformation.
            event_timestamp_column (Optional[str]): The timestamp field of your record. As sliding window aggregation feature assume each record in the source data should have a timestamp column.
            timestamp_format (Optional[str], optional): The format of the timestamp field. Defaults to "epoch". Possible values are:
            - `epoch` (seconds since epoch), for example `1647737463`
            - `epoch_millis` (milliseconds since epoch), for example `1647737517761`
            - Any date formats supported by [SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html). 
            registry_tags: A dict of (str, str) that you can pass to feature registry for better organization. For example, you can use {"deprecated": "true"} to indicate this source is deprecated, etc.
        """
    def __init__(self, name: str, path: str, preprocessing: Optional[Callable] = None, event_timestamp_column: Optional[str]= None, timestamp_format: Optional[str] = "epoch", registry_tags: Optional[Dict[str, str]] = None) -> None:
        super().__init__(name, event_timestamp_column, timestamp_format, registry_tags=registry_tags)
        self.path = path
        self.preprocessing = preprocessing

    def to_feature_config(self) -> str:
        tm = Template("""  
            {{source.name}}: {
                location: {path: "{{source.path}}"}
                {% if source.event_timestamp_column is defined %}
                    timeWindowParameters: {
                        timestampColumn: "{{source.event_timestamp_column}}"
                        timestampColumnFormat: "{{source.timestamp_format}}"
                    }
                {% endif %}
            } 
        """)
        msg = tm.render(source=self)
        return msg

    def __str__(self):
        return str(self.preprocessing) + '\n' + self.to_feature_config()


class JdbcSource(Source):
    def __init__(self, name: str, url: str = "", dbtable: Optional[str] = None, query: Optional[str] = None, auth: Optional[str] = None, preprocessing: Optional[Callable] = None                 ,event_timestamp_column: Optional[str] = None, timestamp_format: Optional[str] = "epoch",registry_tags: Optional[Dict[str, str]] = None) -> None:
        super().__init__(name, event_timestamp_column, timestamp_format, registry_tags)
        self.preprocessing = preprocessing
        self.url = url
        if dbtable is not None:
            self.dbtable = dbtable
        if query is not None:
            self.query = query
        if auth is not None:
            self.auth = auth.upper()
            if self.auth not in ["USERPASS", "TOKEN"]:
                raise ValueError("auth must be None or one of following values: ['userpass', 'token']")

    def get_required_properties(self):
        if not hasattr(self, "auth"):
            return []
        if self.auth == "USERPASS":
            return ["%s_USER" % self.name, "%s_PASSWORD" % self.name]
        elif self.auth == "TOKEN":
            return ["%s_TOKEN" % self.name]

    def to_feature_config(self) -> str:
        tm = Template("""  
            {{source.name}}: {
                location: {
                    type: "jdbc"
                    url: "{{source.url}}"
                    {% if source.dbtable is defined %}
                    dbtable: "{{source.dbtable}}"
                    {% endif %}
                    {% if source.query is defined %}
                    query: "{{source.query}}"
                    {% endif %}
                    {% if source.auth is defined %}
                        {% if source.auth == "USERPASS" %}
                    user: "${{ "{" }}{{source.name}}_USER{{ "}" }}"
                    password: "${{ "{" }}{{source.name}}_PASSWORD{{ "}" }}"
                        {% else %}
                    useToken: true
                    token: "${{ "{" }}{{source.name}}_TOKEN{{ "}" }}"
                        {% endif %}
                    {% else %}
                    anonymous: true
                    {% endif %}
                }
                {% if source.event_timestamp_column is defined %}
                    timeWindowParameters: {
                        timestampColumn: "{{source.event_timestamp_column}}"
                        timestampColumnFormat: "{{source.timestamp_format}}"
                    }
                {% endif %}
            } 
        """)
        msg = tm.render(source=self)
        return msg

    def __str__(self):
        return str(self.preprocessing) + '\n' + self.to_feature_config()
class KafkaConfig:
    """Kafka config for a streaming source
    Attributes:
        brokers: broker/server address
        topics: Kafka topics
        schema: Kafka message schema
        """
    def __init__(self, brokers: List[str], topics: List[str], schema: SourceSchema):
        self.brokers = brokers
        self.topics = topics
        self.schema = schema


class KafKaSource(Source):
    """A kafka source object. Used in streaming feature ingestion."""
    def __init__(self, name: str, kafkaConfig: KafkaConfig):
            super().__init__(name)
            self.config = kafkaConfig

    def to_feature_config(self) -> str:
        tm = Template("""
{{source.name}}: {
    type: KAFKA
    config: {
        brokers: [{{brokers}}]
        topics: [{{topics}}]
        {{source.config.schema.to_feature_config()}}
    }
}
        """)
        brokers = '"'+'","'.join(self.config.brokers)+'"'
        topics = ','.join(self.config.topics)
        msg = tm.render(source=self, brokers=brokers, topics=topics)
        return msg


INPUT_CONTEXT = InputContext()
