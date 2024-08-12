
''' Purpose: continue string manipulation introduction
'''

print()

# operator + when given two string operands produces their concatenation;
# i.e., a new string that is formed by running the two operands together

print( '### operator + performs concatenation' )

a = 'fire'
b = 'fighter'
c = a + b

print( 'a =', a )
print( 'b =', b )

print()

print( 'a + b =', c )

print()

# operator * when one of its operands is a string and the other is an integer,
# produces a new string that is a repeated concatenation of string operand
# indicated by the integer

print( '### * operator produces repeated concatenation' )

m  = '\tWahoo-Wah!\n'       # '\n' = newline chacrater --> included as part of m string
#
n  = 3

# \ is called an escape character. you must use it in '' to indicate a special character immediatly after
# '\t' = tabs character


mn = m * n
nm = n * m

print( 'm = ', m )     # m as it currently stands has a tab chafracter in front of Wahoo-Wah and has a newline
                                # newline gives you that space between m= ... and then n=3
print( 'n = ', n )

print()

print( 'm * n =', nm )
print( 'n * m =',     nm )



