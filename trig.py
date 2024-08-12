
'''generate triplets of base 256 values based on trigometric manipiulations'''

import math 

def red( x, y ) :
    r = math.cos( math.pi * math.sin( math.pi * math.sin( math.pi * math.sin( math.pi * math.cos( math.pi * y * math.sin( math.pi * x ) ) * x ) ) ) )
    r = int( r * 127.5 + 127.5 )
    return r

# create shortcuts from math library's math.sin, cos, and pi elements
from math import sin, cos, pi

def green( x, y ) :
    g = sin( pi * sin( pi * sin( pi * sin( pi * x ) ) * sin( pi * y * x ) * cos( pi * x * x * y * x * x * y ) ) )
    g = int( g * 127.5 + 127.5 )
    return g

def blue( x, y ) :
    b = cos( pi * sin( pi * sin( pi * cos( pi * sin( pi * y ) * sin( pi * y ) ) ) ) * y )
    b = int( b * 127.5 + 127.5 )
    return b

def f( d ) :
    for y in range( 0, d ) :
        for x in range( 0, d ) :
            sx = -( x - d/2 ) / ( d/2 )
            sy =  ( y - d/2 ) / ( d/2 )

            r = red( sx, sy )
            g = green( sx, sy )
            b = blue( sx, sy )

            rgb = ( r, g, b )

            print( '({:3d},{:3d},{:3d})'.format( r, g, b ), end=' ')
        print()

if ( __name__ == '__main__' ) :
    f( 6 )
