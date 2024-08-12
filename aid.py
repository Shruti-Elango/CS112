

''' Purpose: function exploration with list manipulations
'''


def rotate( x ) :
    ''' Updates list x by moving the last element of list x (if any) to the
            beginning of list x (a circular shift)
        Returns None
    '''
    length= len(x)
    if(length >0):
        last= x.pop()
        x.insert (0, last)
    pass

def rotate_k_times( x, k ) :
    ''' Updates list x by performing k circular shifts
        Returns None
    '''
    for i in range (0, k):
        rotate (x)
    pass

def common( x, y ) :
    ''' Returns a new list whose elements are those elements in x that are also in y.
        The function does not modify parameters x and y in any way.
    '''
    listing= []
    for element in x:
        if (element in y):
            listing.append(element)
        else:
            pass
    result = listing
    return result
    pass

if ( __name__ == '__main__' ):    # __name__ is a built in python variable.
    import abet                   #   it is set to the string '__main__' if
                                  #      you are running the file as a program
                                  #   it is set to the name of the file if
                                  #      the file is being imported

    abet.test_rotate()
    abet.test_rotate_k_times()
    abet.test_common()
