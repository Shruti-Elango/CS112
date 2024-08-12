
''' Purpose: test mash.py with a beyonce, dinosaur, and wonder woman on the lawn
'''

import url
import mash

def clean_up( original, back_screen ) :
    ''' Returns a copy of original where pixels similar to the back_screen are set
        to the back_screen
    '''

    new_image = original.copy().convert( 'RGB' )

    nw, nh = new_image.size

    for nx in range( 0, nw ) :
        for ny in range( 0, nh ) :
            nspot = ( nx, ny )
            npixel = new_image.getpixel( nspot )

            if ( mash.similar( npixel, back_screen ) ) :
                new_image.putpixel( nspot, back_screen )

    return new_image

# IMAGE INFO
URL_LAWN = 'http://www.cs.virginia.edu/~cs1112/images/lawn.png'
IMG_LAWN = url.get_image( URL_LAWN )

URL_BEY  = 'http://www.cs.virginia.edu/~cs1112/images/green-beyonce.png'
IMG_BEY  = url.get_image( URL_BEY )
IMG_BEY  = clean_up( IMG_BEY, mash.GREEN )

URL_DINO = 'http://www.cs.virginia.edu/~cs1112/images/green-dino.png'
IMG_DINO = url.get_image( URL_DINO )
IMG_DINO = clean_up( IMG_DINO, mash.GREEN )

URL_WW   = 'http://www.cs.virginia.edu/~cs1112/images/green-ww.png'
IMG_WW   = url.get_image( URL_WW )
IMG_WW   = clean_up( IMG_WW, mash.GREEN )

URL_R2D2 = 'http://www.cs.virginia.edu/~cs1112/images/green-r2d2.png'
IMG_R2D2 = url.get_image( URL_R2D2 )
IMG_R2D2 = clean_up( IMG_R2D2, mash.GREEN )

def test_with_dino() :

    bg = IMG_LAWN.copy().convert( 'RGB')

    bw, bh = bg.size

    sx =  4 * bw // 18
    sy = 12 * bh // 24

    mash_up = mash.combine( bg, IMG_DINO, sx, sy, mash.GREEN )

    mash_up.show()

def test_with_beyonce() :
    bg = IMG_LAWN.copy().convert( 'RGB')

    bw, bh = bg.size

    sx =  5 * bw // 18
    sy = 14 * bh // 24

    mash_up = mash.combine( bg, IMG_BEY, sx, sy, mash.GREEN )

    mash_up.show()

def test_with_ww() :
    bg = IMG_LAWN.copy().convert( 'RGB')

    bw, bh = bg.size

    sx =  7 * bw // 18
    sy = 12 * bh // 24

    mash_up = mash.combine( bg, IMG_WW, sx, sy, mash.GREEN )

    mash_up.show()

def test_with_r2d2() :
    bg = IMG_LAWN.copy().convert( 'RGB')

    bw, bh = bg.size

    sx =  7 * bw // 18
    sy = 16 * bh // 24

    mash_up = mash.combine( bg, IMG_R2D2, sx, sy, mash.GREEN )

    mash_up.show()

def test() :
    test_with_beyonce()
    test_with_dino( )
    test_with_ww()
    test_with_r2d2()

if ( __name__ == '__main__' ) :

    import smashing

    smashing.test()
