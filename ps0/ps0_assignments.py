import math

# gets integers x, y from user and prints x**y and log(x)
def first_asgn():
    try:
        x = int(input('Enter an integer\n>'))
    except ValueError:
        print('Integers only')
        return
    try:
        y = int(input('Enter another integer\n>'))
    except ValueError:
        print('Integers only')
        return
    print(f'x ** y : {x**y}')
    print(f'log(x) : {math.log(x, 2.0)}')

first_asgn()