

'''
Name: Shruti Elango
email: se2ezr
Module beanery -- defines three functions associated with jelly
    bean count manipulation

    Buddies (if any):Cory Davis, Nyota Patel, Seth Lewis
'''

import math

def volume( a, b ) :
    ''' Returns the volume of jelly bean with length a and height b according
        the problem description
    '''

    volume= (5 * math.pi * a * b**2)/24
    return volume
    pass

def count( s, j , f ) :
    ''' Returns the integer number of beans of volume s that can fit a jar
        wth volume j given the loading capacity is f according to the problem
        description
    '''

    jar = round(j * f / s)
    return jar
    pass

def guess( a, b, j ) :
    ''' Returns the number of number jelly beans with length a and height b
        that can fit in a jar with volume j, where the jar loading factor is
        69.8% (i.e., 0.698)
    '''
    volume2 = (5 * math.pi * a * b ** 2) / 24
    jar2 = .698 * j
    full= jar2/volume2
    final = int(full)
    return final
    pass
