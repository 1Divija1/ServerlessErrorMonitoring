import json

def lambda_handler(event, context):
    x = 5.8 - 2.2
    x = round(x,1) #round off for precision
    return x;


#The floating point bug is because of the way the underlying platform is programmed
#to handle floating point numbers
#this comes into play when we care about precision in mathematical logics of our program
#one way to navigate this is to round off the floating point numbers