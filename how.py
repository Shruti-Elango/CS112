
''' Implements test 2 module how.py
'''

def many( s, t ) :
    x= 0
    able= s.split()
    for n in able:
        if t in n:
            x=x+ 1
    return x
    pass

if ( __name__ == "__main__" ) :

    from test2 import test_how
    
    test_how()
