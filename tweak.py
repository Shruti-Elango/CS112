
''' Implements test 2 module tweak.py
'''

def cyanic( opixel ) :
    red, green, blue = opixel
    npixel = (255-red, 0, 255-blue)
    return npixel
    pass

if ( __name__ == '__main__' ) :

    from test2 import test_tweak

    test_tweak()

