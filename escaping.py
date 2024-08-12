
''' Purpose: continue string manipulation introduction
'''

print()

a = 'hello\nworld'  #\n means the rest of the string is on a new line (the newline character)
b = 'a  b'
c = 'a\tb'      # \t means put a tab in the string
d = 'aren\'t'   # \' means that ' is not the end of the string, just a character

#print ( "a = 'petrichor'" )
#print ( "b = 'a  b'" )
#print ( "c = 'a\\tb'" )     #\\ means that the second \ is a regular character
#print ( "d = 'aren\\\'t'" )

print()

print( 'a:', '\'' + a + '\'' )
print( 'b:', '\'' + b + '\'' )
print( 'c:', '\'' + c + '\'' )
print( 'd:', '\'' + d + '\'' )

print()

na = len( a )
nb = len( b )
nc = len( c )   # 'a\tb' --> this has 3 characters! b/c \t is one character!
nd = len( d )

print( 'len( a ):', na )
print( 'len( b ):', nb )
print( 'len( c ):', nc )
print( 'len( d ):', nd )
