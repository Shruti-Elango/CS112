
''' Implements test 2 module how.py
'''

import random

def count( n ) :
    values = [1,2,3,4,5,6]
    x=0
    for i in range(0, n):
        random_value = random.choice(values)
        random_value2= random.choice(values)
        summ= random_value +random_value2
        if summ == 12:
            x=x+1
    return x
    pass

if ( __name__ == "__main__" ) :

    from test2 import test_twelve

    test_twelve()
