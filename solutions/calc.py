import numpy as np

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a+b

def divide(a,b):

    if b == 0:
        print('Division by zero is not allowed, sir ...')
        return np.nan
    
    return a/b


a = float(input('Enter a: '))
b = float(input('Enter b: '))
op = input('Select operation: \n' +\
           '+ - addition\n' +\
           '- - subtraction\n' +\
           '* - multiplication\n' +\
           ': - division\n')

operations = {'+': add,
              '-': subtract,
              '*': multiply,
              ':': divide}

if op not in operations.keys():
    print('This operation is not supported.')
    exit()

result = operations[op](a,b)
print(f'Result: {result}')
