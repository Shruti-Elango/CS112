
''' Purpose: support image greyscaling transformation
'''

def grey( opixel ) : 
    ''' Returns a new pixel whose RGB values are (m, m, m) where m is
        is the integer cast of .299r + .587g + .114b, where r, g, and b
        are the RGB values of pixel opixel
    '''
    red, green, blue = opixel
    m= .299*red + .587*green + .114*blue
    m= int(m)
    npixel = (m,m,m)
    return npixel
    pass

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    new_image = manip( original, color=grey )

    new_image.show()
