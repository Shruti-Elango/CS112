''' Purpose: support a palette reduction image transformation
'''

def distance( p1, p2 ) :
    ''' Returns the distance between p1 and p2
    '''

    pass

def closest( opixel ) :
    ''' Returns the pixel in PALETTE8 to which opixel is closest
    '''

    PALETTE8 = [ (  0,  0,  0), (255,255,255), (  0,255,  0), (  0,  0,255),
                 (255,  0,  0), (255,255,  0), (255,  0,255), (  0,255,255) ]

    pass

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    im = manip( original, color=closest )

    im.show()
