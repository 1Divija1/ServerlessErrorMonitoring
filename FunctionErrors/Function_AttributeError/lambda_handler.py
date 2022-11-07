import json

def lambda_handler(event, context):
    x=3
    x.merge(100)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
