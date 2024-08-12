
''' Purpose: support image clockwise transformation
                           ---------
'''

def rotate( original ) :
    ''' Return the size of the new image when performing a clockwise
        transformation of the original                     ---------
    '''
    nw, nh = original.size
    rw= nh
    rh= nw
    return (rw, rh)
    pass

def find( nspot, nw, nh ) :
    ''' Returns the counter-clockwise correspondent location of nspot in the
                    -----------------
        original, where nw and nh are the dimensions of the new image
    '''
    nw, nh = original.size
    nx, ny=nspot
    x= ny
    y= (nh-1)-nx
    ospot= (x,y)
    return ospot
    pass

if ( __name__ == '__main__' ) :

    import url
    from manip import manip

    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original, size=rotate, where=find )

    new_image.show()
