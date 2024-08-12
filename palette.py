
''' Purpose: support image mirroring transformation
'''

B        = [ (0,0,0) ]
BW       = B + [ (255,255,255) ]
BWRGB    = BW + [ (0,255,0), (0,0,255), (255,0,0) ]
BWRGBMCY = BWRGB + [ (255,255,0), (255,0,255), (0,255,255) ]
PALETTE  = BWRGBMCY

def set_palette( p ) :
    ''' Sets the default palette to palette p
    '''
    global PALETTE

    PALETTE = p

def closest( opixel ) :
    ''' Returns the pixel closest to opixel in PALETTE
    '''
    global PALETTE
    pale= [(0,0,0),(255,255,255),(0,255,0),(0,0,255),(255,0,0),(255,255,0), (255, 0, 255), (0,255,255)]
    distance_list =[]
    for p in pale:
        value = distance(opixel, p)
        distance_list.append(value)
    smallest_distance= min(distance_list)
    smallest_distancevalues= distance_list.index(smallest_distance)
    npixel= pale[smallest_distancevalues]
    return npixel
    pass

def distance( p1, p2 ) :
    ''' Returns the distance between pixels p1 and p2
    '''
    r1, g1, b1 = p1
    r2, g2, b2 =p2
    dista = abs(r1-r2)+abs(g1-g2)+ abs(b1-b2)
    return dista
    pass

if ( __name__ == '__main__' ) :

    import url
    from manip import manip
    
    # get web image of interest
    link = "http://www.cs.virginia.edu/~cs1112/images/mandrill/full.png"

    original = url.get_image( link )

    palettes = [ B, BW, BWRGB, BWRGBMCY ]

    for p in palettes :
        set_palette( p )

        im = manip( original, color=closest )

        im.show()
