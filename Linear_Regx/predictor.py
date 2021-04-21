# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:32:40 2019

@author: naresh.gangiredd
"""

import os
import json
import flask
import time
# from pyarrow import feather
#from boto3.s3.connection import S3Connection
#from botocore.exceptions import ClientError
#import pickle
# import modin.pandas as pd
from catboost import CatBoostClassifier


import logging

#Define the path
# prefix = '/opt/ml/'
# model_path = os.path.join(prefix, 'model')
# logging.info("Model Path" + str(model_path))
boost = CatBoostClassifier(iterations=1000, depth=5, learning_rate=0.1)
# Load the model components
boost.load_model('catboost.pkl')
logging.info("Regressor" + str(boost))

# The flask app for serving predictions
app = flask.Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    try:
        #regressor
        status = 200
        logging.info("Status : 200")
    except:
        status = 400
    return flask.Response(response= json.dumps(' '), status=status, mimetype='application/json' )

@app.route('/invocations', methods=['POST', 'GET'])
def transformation():
    # Get input JSON data and convert it to a DF
    input_json = str(flask.request.get_data(as_text=True))
    data = input_json.split(',')

    print(input_json)
    
    predictions = int(boost.predict([float(data[0]),float(data[1]), float(data[2]), str(data[3]),  float(data[4]), \
        float(data[5]),  str(data[6]),str(data[7])]))

    # Transform predictions to JSON
    result = {
        'output': predictions
        }

    resultjson = json.dumps(result)
    return flask.Response(response=resultjson, status=200, mimetype='application/json')
