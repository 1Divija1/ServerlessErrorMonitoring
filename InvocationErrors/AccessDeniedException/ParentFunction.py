import json
import boto3
 
# Define the client to interact with AWS Lambda
client = boto3.client('lambda')
 
def lambda_handler(event,context):
 
    # Define the input parameters that will be passed
    # on to the child function
    inputParams = {
        "ProductName"   : "iPhone SE",
        "Quantity"      : 2,
        "UnitPrice"     : 499
    }
 
    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-west-2:056648651098:function:ChildFunction',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(inputParams)
    )
 
    responseFromChild = json.load(response['Payload'])
 
    print('\n')
    print(responseFromChild)
    
#This code is referenced from the site "https://www.sqlshack.com/calling-an-aws-lambda-function-from-another-lambda-function/"
#Our goal was to explore the possible errors due to resource-based and identity-based policy and role assignments in AWS lambda
 