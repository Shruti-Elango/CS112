
''' Purpose: introductory take on examining a table of values
'''
import url
BASE_FOLDER = 'http://www.cs.virginia.edu/~cs1112/words/'
file_name = input( 'Enter file name: ' )
word = input('Enter word: ')
link = BASE_FOLDER + file_name # Assemble the full link using folder + file
# Webpage text is stored as a string in variable text
text = url.get_contents( link )
print( 'Text', text )
words = text.split() # Get a list of words from the text file
print( 'Words', words )
count_word = words.count( word ) # Count the number of times the word occurs
# in your list of words
number_words = len( words ) # Length of words list
fraction = count_word / number_words

print( count_word )
print( number_words )
print( fraction )
#
# s = 'peace'
# s.upper() # This code does not change the value of s - it's immutable.
# print( s )