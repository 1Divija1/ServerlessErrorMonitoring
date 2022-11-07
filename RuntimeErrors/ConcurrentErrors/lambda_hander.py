import json
import uuid
 
def lambda_handler(event, context):
    a=5
    while(True):
        a
        
#If the reserved concurrency limit is set to 'n'
#When this function is invoked for the (n+1)th time concurrently
#Lambda throws a 'rate exceeded' error