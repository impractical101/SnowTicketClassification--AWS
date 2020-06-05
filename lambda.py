import boto3
import os
import ctypes
import uuid
import pickle
from sklearn.externals import joblib
import sklearn
import json


for d, _, files in os.walk('lib'):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

bucket = 's3_bucket'
key = 'classifier'

s3_client = boto3.client('s3')

def handler(event, context):    #handler function which will handle every incoming input
    print((event.get('Records')[0]).get('body'))
    ticketdescription = str((event.get('Records')[0]).get('body'))
    X_test=[]
    X_test.append(ticketdescription)
    bucket = 's3_bucket'    #Loading model
    key = 'classifier.pkl'
    download_path = '/tmp/classifier.pkl'
    s3_client.download_file(bucket, key, download_path)
   
    loadedmodel = joblib.load('/tmp/classifier.pkl')
    class_predicted = (loadedmodel.predict(X_test).tolist())[0]
    print("class_prediced : ", class_predicted)

    pred_probabs = (loadedmodel.predict_proba(X_test).tolist())[0]
    print(pred_probabs)

    pred_json = json.dumps({'class_predicted': class_predicted, 'predict_proba':pred_probabs})
    print(pred_json)

    sqs = boto3.resource('sqs')
    #Using queue to store the incoming and classified tickets 
    queue = sqs.get_queue_by_name(QueueName='classified_support_tickets')
    response = queue.send_message(MessageBody=json.dumps({'ticketdescription': ticketdescription,'class_predicted': class_predicted , 'conf': pred_probabs[0]}))
    return pred_json   #return the Json Object to Snow
