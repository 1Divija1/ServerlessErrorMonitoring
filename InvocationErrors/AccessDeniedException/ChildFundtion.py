import json
import uuid
 
def lambda_handler(event, context):
    #1 Read the input parameters
    productName = event['ProductName']
    quantity    = event['Quantity']
    unitPrice   = event['UnitPrice']
 
    #2 Generate the Order Transaction ID
    transactionId   = str(uuid.uuid1())
 
    #3 Implement Business Logic
    amount      = quantity * unitPrice
 
    #4 Format and return the result
    return {
        'TransactionID' :   transactionId,
        'ProductName'   :   productName,
        'Amount'        :   amount
    }
#This code is referenced from the site "https://www.sqlshack.com/calling-an-aws-lambda-function-from-another-lambda-function/"
#Our goal was to explore the possible errors due to resource based and identity based policy and role assignments in AWS lambda
