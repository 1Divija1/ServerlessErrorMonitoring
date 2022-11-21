def lambda_handler(event, context):

    s = []
    for i in range(10):
       for j in range(10):
           for k in range(10):
               s.append("More")

    print(s)