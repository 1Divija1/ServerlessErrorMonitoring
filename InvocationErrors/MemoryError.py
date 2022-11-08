def lambda_handler(event, context):
    s = []
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                s.append("More")
    print(s)
