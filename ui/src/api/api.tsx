import Axios from "axios";
import { IFeature } from "../models/feature";

const API_ENDPOINT = "https://feathr-dev-api.azurewebsites.net";

export const fetchFeatures = async (page: number, limit: number, keyword: string) => {
  return Axios.get<IFeature[]>(`${ API_ENDPOINT }/features`,
    {
      params: { 'keyword': keyword, 'page': page, 'limit': limit },
      headers: {}
    })
    .then((response) => {
      return response.data
    })
};

export const createFeature = async (feature: IFeature) => {
  return Axios.post(`${ API_ENDPOINT }/features`, feature,
    {
      headers: { "Content-Type": "application/json;" },
      params: {},
    }).then((response) => {
    return response;
  }).catch((error) => {
    return error.response;
  });
}

export const fetchFeature = async (id: string) => {
  return Axios.get<IFeature>(`${ API_ENDPOINT }/features/${ id }`, {}).then((response) => {
    return response.data
  })
};

export const deleteFeature = async (id: string) => {
  return await Axios.delete(`${ API_ENDPOINT }/features/${ id }`,
    {
      headers: { "Content-Type": "application/json;" },
      params: {},
    }).then((response) => {
    return response
  }).catch((error) => {
    return error.response
  });
};

export const updateFeature = async (feature: IFeature, id: string) => {
  feature.id = id;
  return await Axios.put(`${ API_ENDPOINT }/features/${ id }`, feature,
    {
      headers: { "Content-Type": "application/json;" },
      params: {},
    }).then((response) => {
    return response
  }).catch((error) => {
    return error.response
  });
};
