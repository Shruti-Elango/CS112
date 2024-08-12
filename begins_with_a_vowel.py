
''' Purpose: use if-else statement
'''

# define helpful constant
VOWELS = "aeiou"

# get input text and put into canonical form
text = input( 'Enter text: ' )

text = text.strip()

text = text.lower() # bcs all characters in VOWELS is lowercase

# determine its first character
first_character = text[0]
print('first_character=', first_character)

# determine whether first character is a vowel ---> need if/else statement?
# look in first char --> look in VOWELS --> if first char in VOWELS
# if it is in VOWELS: then print yes?
# otherwise (not in VOWELS) : then print no?

if (first_character == VOWELS):
    #first char is vowel
    print ('Yes')
    # first_character is a single character
    # VOWELS is a string length 5
    # therefore, first_character is never == to VOWELS
    # we want to know whether first_character is in VOWELS
    # in: take a substring an check whether that substring/char is in the second string
else:
    # first char not a vowel
    print('No')
