

''' Implements module check.py for test 2
'''

def in_order( x ) :

    if (x==sorted(x)):
        result =True
    else:
        result= False
    return result
    pass

#way 2
    n=len(x)
    # make a guess
    guess = True
    for i in range (0, n-1):
        v1=x[i]
        v2=x[i+1]
        if (v1>v2):
            guess= False
            return False

    return guess

if ( __name__ == "__main__" ) :

    import run

    run.test_in_order()
