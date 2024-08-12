
''' Purpose: provide simple testing of the hodge module
'''

import hodge

#testing summation()

n1 = 5
n2 = 1
n3 = 0

s1 = hodge.summation( n1 )
s2 = hodge.summation( n2 )
s3 = hodge.summation( n3 )

output1 = "summation( " + str( n1 ) + " ): " + str( s1 )
output2 = "summation( " + str( n2 ) + " ): " + str( s2 )
output3 = "summation( " + str( n3 ) + " ): " + str( s3 )

print( output1 )
print( output2 )
print( output3 )
print()

for p in [ 0.350, .005, 1.0 ] :
    a = hodge.sample( p )
    if ( type( a ) == type( 1112 ) ) :
        print( 'sample(', p, ') =', a )
    else :
        print( 'sample(', p, ') did not return an integer value' )

print()

for s in [ 'oxen', 'urchin', 'mink', 'rabbit', 'lynx' ] :
    r = hodge.has_vowel( s )
    if ( type( r ) == type( True ) ) :
        print( 'has_vowel(', s, ') =', r )
    else :
        print( 'has_vowel(', s, ') did not return logical True or False' )
