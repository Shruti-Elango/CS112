
''' Purpose: better experience functional development
'''

from PIL import Image

# helpful constants
SIMILARITY_THRESHOLD = 85                # minimum distance to be dissimilar
GREEN                = ( 0, 255, 0 )     # back screen color

def distance( p1, p2 ) :
    ''' Returns the distance between p1 and p2 RGB values
    '''

    pass

def similar( p1, p2 ) :
    ''' Returns whether the distance between pixels p1 and p2 is less than the
        similarity threshold
    '''

    pass

def is_background( p, back_screen ) :
    ''' Returns whether p is similar to the back_screen color
    '''

    pass

def inbounds( spot,  img ) :
    ''' Returns whether spot lies on img.
    '''

    pass

def colorable( spot, img, p, back_screen ) :
    ''' Returns whether both
            spot is a location on img and
            color p is not similar to color back_screen
    '''

    pass

### DO NOT MODIFY THE BELOW CODE

def combine( bg, fg, sx, sy, back_screen ) :
    ''' Returns mash up of background image bg and foreground image fg, where
        the pixels in fg that are dissimilar to back_screen are copied on top
        of the background.
    
        The mash up uses location (sx, sy) as the spot in the background to
        start the lay over of fg.
    '''

    bw, bh = bg.size                      # size of background image
    fw, fh = fg.size                      # size of foreground image

    copy      = bg.copy()                 # get a copy of background image
    new_image = copy.convert( 'RGB' )     # to be the basis of new image

    for fx in range( 0, fw ) :            # consider every (fx, fy)
        for fy in range( 0, fh ):         # possibility of the new image

            fspot = ( fx, fy )            # name spot (fx, fy )

            fpixel = fg.getpixel( fspot ) # get the pixel at fspot

            nx = sx + fx                  # determine spot on new image
            ny = sy + fy                  # to paint fpixel
            nspot = ( nx, ny )

            # check whether fpixel should be painted on new image at nspot
            if ( colorable( nspot, new_image, fpixel, back_screen ) ) :
                new_image.putpixel( nspot, fpixel )

    return new_image                      # return the mash up

if ( __name__ == '__main__' ) :

    import smashing

    smashing.test_with_dino()
    smashing.test_with_beyonce()
    smashing.test_with_ww()
