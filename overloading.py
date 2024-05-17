from multipledispatch import dispatch

# passing two parameter
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

# passing three parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

# calling product method with 2 arguments
product(2, 5) # this will give output of 10

# calling the product method/function  with 3 arguments
product(2, 5, 2) # this will give output of 20