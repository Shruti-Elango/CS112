
''' Purpose: help with understanding that functions are first class
'''

def black() :
    print( "Black" )


def white() :
    print( "White" )


def run( f ) :
    print('f =', f)
    f()


if ( __name__ == "__main__" ) :

    run( black )
    run( print )
    run( white )
