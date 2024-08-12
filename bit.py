
''' Implements module bit.py for test 2
'''

import random

def ter( n, k ) :
    values =[]
    for i in range (0, n):
        random_value= random.randrange(0,k)
        values.append(random_value)
    return values
    pass


if ( __name__ == "__main__" ) :
    import run

    run.test_ter()
