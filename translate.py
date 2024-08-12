
''' Purpose: translate user text to English
'''

import url

DEFAULT_URL = 'http://www.cs.virginia.edu/~cs1112/words/babel'

DEFAULT_DICTIONARY = url.get_dictionary( DEFAULT_URL )

def passage( text, dictionary = DEFAULT_DICTIONARY) :
    ''' returns a translation of text according to dictionary, where
        text may have embedded \n's
    '''
    #convert text into lines to translate each line at a time
    #split on new line character ('\n')
    lines= text.split("\n")
    result= ''
    for phrase in lines:
        convert = line(phrase, dictionary)  #function to trandlate a line and return the translation
        result= result + convert +'\n'
    return result

    pass

def line( string, dictionary = DEFAULT_DICTIONARY ) :
    ''' returns a translation of string according to dictionary, where
        string is composed of zero or more words
    '''
    words= string.split()
    result = ''
    for w in words:
        conversion = word (w, dictionary)
        result = result + conversion + ' '
    return result
    pass

def word( string, dictionary = DEFAULT_DICTIONARY) :
    ''' returns a translation of the string according to dictionary,
        where string is composed of a single word.  if the translation
        is unknown the function return the word within <>
    '''
    if (string in dictionary):
        result = dictionary.get(string)
    else:
        result = '<' + string + '>'

    return result
    pass

if ( __name__ == '__main__' ) :
    translation = word( 'lapiz' )
    print( translation )
    print()

    translation = line( 'como esta eso' )
    print( translation )
    print()

    translation = passage( 'tun vous savez hvor\nmi pencil ist' )
    print( translation )
    print()

    DIGIT_URL = 'http://www.cs.virginia.edu/~cs1112/words/digits'

    d = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

    translation =  passage( '0 O 1 2 3 4 5', dictionary = d )
    print( translation )
    print()

    text = ''' dubailte dubailte kesusahan und guaio
               umlilo adolebitque und ketel bombolla
               umucu di una pantanoso neidr
               dans der ketel bouyi und cuire
               oog di tritons und kaki di rano
               yun di fledermoyz und lingua di chien
               viperae foarke und blyn cuc stik
               moo fotur und ovlet tis
               pre eng viehatys di voimakas guaio
               mag un inferno salda bouyi und bombolla
    '''

    translation = passage( text )
    print( translation )
