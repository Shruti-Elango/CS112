
''' Purpose: practice function chresthomathics``
'''

import math

def summation( n ) :
    ''' For integer parameter n, returns the sum of 1 + ... + n.
    '''

    sum = 0
    for i in range (0,n):
        sum = sum +1 + i
    result= sum

    return result

def sample( d ) :
    ''' Returns an integer estimate of the age of a fossil with a carbon-12 to
        carbon-14 ratio of d
    '''
    result = round( -8268.3982 * math.log(d))
    return result
    pass

def has_vowel( w ) :
    ''' Returns True or False depending whether a lower-case vowel is part
        of string d
    '''
    #result = True
    if ('a' in w) or ('e' in w) or ( 'i' in w) or('o' in w) or ('u' in w):
        result = True
    else:
        result = False
    return result

    pass

