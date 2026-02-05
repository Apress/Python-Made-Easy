def function_one():
    return 1

def function_two():
    return 2

def print_function(func):
    print(func())

print_function(function_one) # prints 1
print_function(function_two) # prints 2