
''' Implements test 2 module two.py
'''

def add( x, y ) :
    long= len(x)
    long2= len(y)

    brack= []
    for n in range (0, long):
        indexingx=x[n]
        indexingy=y[n]
        integer= int(indexingx)
        integer2= int(indexingy)
        add= integer+integer2
        brack.append((add))
    return brack
    pass

if ( __name__ == "__main__" ) :

    from test2 import test_two
    
    test_two()
