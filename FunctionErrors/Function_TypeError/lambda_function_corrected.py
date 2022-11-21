def lambda_handler(event, context):
    my_integer = 1
    my_second_integer = 2
    my_string = "Hello World"
    my_second_string = "How are you all?"
    my_integer_result = my_integer + my_second_integer
    my_string_result = my_string + my_second_string
    print(my_integer_result)
    print(my_string_result)
