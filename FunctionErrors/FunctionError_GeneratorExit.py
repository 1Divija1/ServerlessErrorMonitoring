import json

def lambda_handler(event, context):
    def generator():
            yield 1

    g = generator()
    print(next(g))
    print(next(g))