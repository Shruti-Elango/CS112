

''' Implements test 2 module onds.py
'''

def sec( h, m ) :
    hours= h * 60* 60
    minutes = m * 60
    final = hours + minutes
    return final
    pass

if ( __name__ == "__main__" ) :

    from test2 import test_onds

    test_onds()
