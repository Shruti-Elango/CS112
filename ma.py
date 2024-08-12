
''' Implements test 2 module ma.py
'''

def sig( d ) :
    a=0
    b=0
    c=0
    for n in d:
        x= len(n)
        for y in n:
            if y<0:
                a=a+1
            elif y== 0:
                b=b+1
            elif y>0:
                c=c+1
    new= [a,b,c]
    return new

    pass

if ( __name__ == "__main__" ) :

    from test2 import test_ma

    test_ma()
