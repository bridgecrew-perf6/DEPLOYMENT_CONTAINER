
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request
import cv2
import numpy as np
import json
import os
from model_config import load_model_mappings
import requests
import ast
# Flask constructor takes the name of 
# current module (__name__) as argument.


model_config_files={}
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/prediction',methods=["POST",'GET'])
# ‘/’ URL is bound with hello_world() function.
def predictions():
    data=request.data
    data=data.decode("utf-8")
    data=ast.literal_eval(data)
    header=request.headers['Content-Type']

    img= cv2.resize(cv2.imread(os.path.join('data','images',data["image"]),0),(28,28))
    json_data = json.dumps({"signature_name": "serving_default", "instances": np.array(img).reshape(1,28,28,1).tolist()})
    headers = {"content-type": header}
    
    url_var= os.path.join('http://modelservice:8501/v1/models',str(data["model_name"]))+':predict'
    json_response = requests.post(url_var, data=json_data, headers=headers)

    
    
    if(str(data["model_name"]) in model_config_files.keys()):
        classes= model_config_files[str(data["model_name"])]
        print('not_loaded_again')

    else:
        model_config_files[str(data["model_name"])]=load_model_mappings(str(data["model_name"]))

        classes= model_config_files[str(data["model_name"])]
        print('here loaded')



    predictions_score = json.loads(json_response.text)['predictions']


    responses={}
    responses['Final Prediction'] = {'class':classes[np.argmax(predictions_score)],'confidence':np.max(predictions_score)}
    
    return responses
  
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()