
''' Purpose: consider string casing functions
'''

text = input( 'Enter text: ' )

print()

print( 'text:', text )

print()

# produce case variants of input text
text_c = text.capitalize() # first letter in string as uppercase
text_l = text.lower() #lowercase everything
text_u = text.upper() #uppercase everything
#leave () empty- doesnt need anything
# gives a new version of the string, dont need to modify old string

print( 'text.lower():', text_l, '       # all lower case' )
print( 'text.upper():', text_u, '       # all upper case' )
print( 'text.capitalize():', text_c, '  # initial character capitalized, rest lower case' )
