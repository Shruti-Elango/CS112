''' Purpose: continue introduction to functions
'''

def is_factor( x, y ) :
    ''' Parameters x and y are integers. The function returns whether y is a
        factor of x.
    '''

    # compute remainder of x divided by y
    rem = x % y

    # check it out
    if ( rem == 0 ) :   # check whether remainder is 0
        result = True   # if it is, return value is True
    else: 
        result = False  # if it is not, return value is False

    # return determination
    return result

    return 'tgif'



def is_prime( x ) :
    ''' Parameter x is am integer. The function returns whether x is prime;
        i.e., its only factors are 1 and itself.
    '''

    result = True #assume number is prime at first

    for i in range (2, x):
        if (is_factor( (x, i) == True)):
            result = False
            # once we found the first thing thats a factor of x, we want to exit the function immediatly!
            # we have the answer right now, so we don't want to keep going in the for loop
            #return result
    return result

def are_relative_primes( x, y ) :
    ''' Parameters x and y are integers. The function returns whether x and
        y are relatively prime; i.e., whether y is not a factor of x and
        vice-versa.
    '''
# NOT ENOUGH TIME TO FINISH!
    # test if factor (x,y) --> false
    elif (is_factor( (y, x) == True)):
        result = False
    else:
        result = True
    return result
