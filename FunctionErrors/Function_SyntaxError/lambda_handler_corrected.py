import json

def lambda_handler(event, context):
    x = 1  #corrected the indentation in the statement that was causing the error
    y = 0
    assert y != 0
    print(x / y)
    