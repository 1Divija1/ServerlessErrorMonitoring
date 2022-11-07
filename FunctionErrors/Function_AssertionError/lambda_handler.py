import json

def lambda_handler(event, context):
    x = 3
    y = 3
    assert y != x
    print(x / y)