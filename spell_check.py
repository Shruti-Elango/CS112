

''' Purpose: spell check a line of input
'''

# import get module for url supoprt
import url

# define link for spelling dictionary
WORDS_FOLDER_URL   = "http://www.cs.virginia.edu/~cs1112/datasets/words/"
SPELLING_LIST_URL  = WORDS_FOLDER_URL + "most-common"

# get the spelling list as a list of words
text = url.get_contents( SPELLING_LIST_URL )
spellings = text.split()

# get the user text as a list of words
reply = input( "Enter text: " )
reply = reply.lower() # words on string not list- want bcs our list of common words contain all words with lowercase
words = reply.split() # get each word in the text into its own element in a list

# consider the words one by one -- determine whether current word is misspelled.
for word in words:
    # check if all word correctly spelled
    if (word not in spellings):
# if correctly want to print word
        print(word)

# all done
