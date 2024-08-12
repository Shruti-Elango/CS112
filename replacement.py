
''' Purpose: consider string replace() functions
'''

text = input( "Enter text: " )

s = input( "Enter substring (s): " )

r = input( "Enter substring (r): " )

print()

# get version of text with occurrences of s replaced with r

modified_text = text.replace( s, r )

print( "text.replace( s, r ):", modified_text, "   # text's s's replaced with r's" )
# x is the substring we want to replace
# y is the substring we are substituting in
# look for all character in s in the string tect and replace with r
# if r is an empty string it puts "nothing" where all of s is
# looks for s exactly
