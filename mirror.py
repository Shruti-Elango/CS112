
''' Purpose: support image mirroring transformation
'''

def mirror( nspot, nw, nh ) :
    ''' Returns the correspondent of nspot in its nw x ny image
        in the unmirrored original
    '''

    pass

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original, where=mirror )

    new_image.show()
