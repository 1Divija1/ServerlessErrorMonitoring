import json
import datetime
import urllib
import boto3


def process_purchase(message, context):
    # TODO implement

    print("received messsage from step fn")
    print(message)

    response = {}
    response['TransactionType'] = message['TransactionType']
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    response['Message'] = "Hello from process purchase lambda"
    
    raise Exception("Lambda error")

    return response