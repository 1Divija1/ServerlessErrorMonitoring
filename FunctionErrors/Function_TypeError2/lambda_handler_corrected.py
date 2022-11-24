import json
def lambda_handler(event, context):
    c=1
    d=2
    add(c,d)
def add(c,d): #removed the extra argument that was causing the error
    return c+d