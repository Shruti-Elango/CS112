
''' Purpose: better experience functional development

    Buddies (if any): Francis Driscoll, Aryan Pandya, Maximus Maldonado
'''

# necessary import

def future_me( age, y ) :
    ''' Function future_me( a, y ): how old a person whose now a years-old will be
        in year y
    '''
    math = (y - 2021) + age
    return math
    pass

# --------------------------------------------------------------------

def manhattan_distance( a1, s1, a2, s2 ) :
    ''' Function manhattan_distance( a1, s1, a2, s2 ): returns the
        approximate distance in miles between a person at the corner
        avenue a1 and street s1 in Manhattan and a person at the corner
        of avenue a2 and street s2 also in Manhattan.
    '''
    ave = abs(a2-a1)
    street = abs(s2-s1)
    street_len = (1/20) * street
    ave_len = (3/20) * ave
    length= street_len + ave_len
    return length
    pass



# --------------------------------------------------------------------

def relate( x, y ) :
    ''' Function relate( x, y ): returns '<', '==', or '>', depending on the
        alphabetical relationship between strings x and y.
    '''
    x=x.lower()
    y= y.lower()
    if x>y:
        return '<'
    elif x<y:
        return '>'
    elif x==y:
        return '=='
    pass




# --------------------------------------------------------------------

def youngest( y ) :
    ''' Function youngest( y ): returns the youngest acceptable integer age
        for a y-year old to date; i.e., the age must be at least seven years
        older than half of a y-year old
    '''
    new = (0.5*y) + 7
    new2 = int(new)
    return new2
    pass



# --------------------------------------------------------------------

def is_dateable( y1, y2 ) :
    ''' Function is_dateable( y1, y2 ): returns True or False whether
        a y2-year old is an acceptably-aged date for a y1-year old.
    '''
    age= youngest(y1)
    if y2 >= age:
        return True
    elif y2 < age:
        return False
    pass



# --------------------------------------------------------------------

def mutually_dateable( y1, y2 ) :
    ''' Function mutually_dateable( y1, y2 ): returns True or False
        whether both a y2-year old is an acceptably-aged date for a 
        y1-year old and vice-versa.
    '''
    if is_dateable(y1, y2) and is_dateable(y2, y1):
        return True
    else:
        return False
    pass


# --------------------------------------------------------------------

def middle( s ) :
    ''' Function middle( s ): if the length of s is odd, the function
        returns the middle character of s; otherwise, the function returns
        the two middle characters of s.
    '''
    odd_even= len(s) % 2
    if odd_even == 1:
        index = len(s) //2
        return s[index]
    else:
        index2= (len(s) / 2) - 1
        index2 = int(index2)
        index3= index2 + 1
        index3= int(index3)
        letter= s[index2] + s[index3]
        return letter
    pass



