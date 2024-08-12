
''' Purpose: translate user text to English
'''

# get access to url support
import url

# CS 1112 translation dictionary -- entries are of form: word,translation
BABEL_FISH_URL = "http://www.cs.virginia.edu/~cs1112/words/babelfish"

# delimiters for unknown words
UNKNOWN_WORD_DELIMITER = "?"

# get contents of babel fish url as a dictionary
babelfish_dictionary = url.get_dictionary(BABEL_FISH_URL)

# get the user text to be translated
reply = input( "Enter phrase to be translated: " )

# convert reply into a list of words
words_to_be_translated = reply.split()

# initialize translation accumulator
# look at each word in the input sentence, find the translation and then add the translation
translation = ' ' #start with empty string

# process the words for translation one by one. each word contributes to the translation

for current_word in words_to_be_translated :
    # whether current word is in the dictionary, determines our translation action
    if (current_word in babelfish_dictionary): # if current_word doesn exist? error
        output_word= babelfish_dictionary.get(current_word)
    else:
        output_word= '_' + current_word + '_'

    translation = translation + output_word+ ' '

# print translation
    print( translation )
