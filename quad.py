
''' Purpose: better experience functional development

    Buddies (if any): Chris Kim, Jordan Giles
'''

# helpful named strings

PUNCTUATION = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
WHITE_SPACE = ' \t\n\r\v\f'
EXTRANEOUS  = PUNCTUATION + WHITE_SPACE

def to_lower( strings ) :
    ''' Returns a new list whose elements are lower case versions of
        those in strings
    '''
    result = []
    for string in strings:
        lower_string = string.lower()
        result.append(lower_string)
    return result
    pass

def unique( strings ) :
    ''' Returns a new version of strings without any duplicate values
    '''

    result = []
    for string in strings:
        if (string not in result):
            result.append(string)

    return result

    pass


def cleanup( strings ) :
    ''' Returns a new version of strings where the corresponding
        elements have leading and trailing extraneous characters
        (punctuation or whitespace) removed
    '''
    result = []
    for string in strings:
        cleaned_up = string.strip (EXTRANEOUS)
        result.append (cleaned_up)
    return result

    pass

def canonical( strings ) :
    ''' Returns a new version of strings without duplicate values
        where the corresponding elements have leading and trailing
        extraneous characters (punctuation or whitespace) removed
        and are in lowercase
    '''
    result = unique(cleanup(to_lower(strings)))
    return result
    pass
