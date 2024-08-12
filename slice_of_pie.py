''' Purpose: remind you about string indexing.
             introduce string slicing
'''

# operator [] is the sequence index operator. Our use so far
# is to get an individual character from a string

s = input( 'Enter favorite pie: ' )

t = input( 'Enter two indices: ' )

i, j = t.split()                # i= the first index, j= the second index
i, j = int( i ), int( j )

print( 's:', s )
print( 'i:', i )        # is the number
print( 'j:', j )        # is the other number

print()

# string indexing: some_string[index] ---
print( 's[ i ]: ', s[ i ] )
print( 's[ j ]: ', s[ j ] )

print()

# get slices of s using the slicing operator :
# get a substring starting from position i and go up to but not including the character at index j
# so includes character at position i and up to index j-1
# if i=3 and j=15 --> includes all character starting fromindex 3 through character at index 14
slice1 = s[ i : j ]     # we store the substring in a variable so we can use it later
# the second number after : is optional. If you dont give a second number then it goes all the way to the end of the string s
slice2 = s[ i : ]
# also optional is putting number in front of : --> then start at the very beginning (0) an up to but not including j
slice3 = s[ : j ]
# also both are optional --. makes a new copy of the entire string! starts at index 0 and goes up to the end of the string s
slice4 = s[ : ]

# if s= 'apple'
#indice  01234
# s[1:3] = 'pp'
# s[:3] = 'app'
# s[1:] = 'pple'
# s[:] = 'apple'
# strings are immutable! Cannot change anything, only returns a new copy.
print( 's[ i : j ]:', slice1 )
print( 's[ i :   ]:', slice2 )
print( 's[   : j ]:', slice3 )
print( 's[   :   ]:', slice4 )

# to include j you can do j+1 in the substring slicing
