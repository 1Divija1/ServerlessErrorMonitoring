import json

def lambda_handler(event, context):
    x = 3
    y = 3
    assert y == x  #assertion is true because x=y and hence the assertion error is avoided
    print(x / y)