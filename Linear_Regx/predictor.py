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
    input_json = flask.request.get_json()
    print(input_json)
    # input = input_json['input']['exp1']
    predictions = float(boost.predict([1000000, 50, 1, 'maybe', 0, 0, 'Owner', 'Owner']))

    # Transform predictions to JSON
    result = {
        'output': predictions
        }

    resultjson = json.dumps(result)
    return flask.Response(response=resultjson, status=200, mimetype='application/json')
