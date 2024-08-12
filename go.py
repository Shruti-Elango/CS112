
''' Purpose: do some functions produces lists from a string
'''

def ints( ns ) :
    ''' Returns list of integers corresponding to the integer substrings in ns.
    '''
    numeric_strings = ns.split()

    result= [] # list of ints that's associated with the string ns
    for string in numeric_strings:
        number= int(string)
        result.append(number)

    return result
    pass
        
def parse_phone_string( pn ) :
    ''' Returns a three-element integer list for string phone # pn:
           1st element: pn area code
           2nd element: pn prefix
           3rd element: pn line number
    '''

    pass
