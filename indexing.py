
''' Purpose: continue string manipulation introduction
'''

print()

#indexing always starts at 0!!!



# Operator [] is the string index operator -- it provides access to
# a string subsequence. Depending upon its operands it is all called
# subscripting and slicing. Here we only care about subscripting.
# The subscript is an index value. In Python index values start at 0.

print( '### [] is the string index operator' )
s = 'sequoia'

n = len( s )

print( 's =', s, )
print( '    0123456' )

print()

print( 'n = len( s ) =', n )

print()

print( '### If the [] operand is an integer value, it is subscripting' )
# [] is the subscripting operator
# you give it an index/a position in the string to get that character, this must be an int
x = s[ 0 ]  # gets the character at index 0 (the very first one)
y = s[ 4 ]  # gets the character at index 4 (the fifth thing)
z = s[ n-1 ]    # n is the length of s (from line 19) n-1 is the very last index of the string

# the last index (number/ position) of the string is ALWAYS length of the string - 1 because indexing starts at 0!!!!!!!
# if string has 7 characters, its length is 7; the last index of the string would be 6 (7 -1 )
print( 's[ 0 ] = ', x )
print( 's[ 4 ] = ', y )
print( 's[ n-1 ] = ', z )
