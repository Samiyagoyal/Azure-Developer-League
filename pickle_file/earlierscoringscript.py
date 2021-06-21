#Driver Code for data Input / Output from REST Endpoint

import json
import numpy as np
import os
import joblib
from azureml.core import Model


def init():
    global model, model_path
    model_path = Model.get_model_path('ngo_recommender')
#     model = joblib.load(model_path)
    

def run(data):
    try:
        # the input json to be of form 
        # { "data" : "NGO - Name", "events": "Event-Description" }
        
        input_data = json.loads(data)['data']
        (sim_mat, titles, indices) = joblib.load(model_path)
        
        def get_recommendations(input_data):
            idx = indices[input_data]
            sim_scores = list(enumerate(sim_mat[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:6]
            ngo_indices = [i[0] for i in sim_scores]
            return titles.iloc[ngo_indices].values
        
        
        result = get_recommendations(input_data)
        result = json.dumps({ "data" : result.tolist()})
        
        # the resultant json is of form 
        # { "data" : ["NGO1-name","NGO2-name","NGO3-name","NGO4-name","NGO5-name"]}
        
        
        return result
    except Exception as e:
        error = str(e)
        return error
