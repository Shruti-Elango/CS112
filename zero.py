
''' Purpose: demonstrate a function side-effect in Python
'''

def out( x) :
    ''' Does ???
    '''

    n = len( x )

    for i in range( 0, n ) :
        x[ i ] = 0

    return
