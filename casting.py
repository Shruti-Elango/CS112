
''' Purpose: introduce casting -- constructing a value of one type
                from a value of  another type

        int( s ): returns the integer constructed from integer numeric
                        string s
        int( d ): returns the integer part of decimal d

        float( s ): returns the decimal constructed from  numeric
                        string s.  there maybe loss of precision

        float( i ): returns the decimal constructed using integer i.
                        there maybe loss of precision
        
        str( x ) : returns a string version of x
'''

# get a hold of the pause module
import pause

# define values for int and float casting
integer_string = '112358' #can only use a SINGLE number
decimal_string = '93.86'
decimal_number = 9.04
integer_number = 1112

# cannot do arithmetic within the int() and float() functions

# get integer conversions
i1 = int( integer_string ) #get the integer version of the value in integer_string
i2 = int( decimal_number ) #get the float version of the string value in decimal_number
#int(x)
# if x is a string integer, it converts it into that integer; ONLY ONE ARGUMENT,
#   ONE STRING REPRENTATION OF AN INTEGER
# if x is a float, it drops the decimal places; no rounding

# get decimal conversions
f1 = float( integer_number )
f2 = float( decimal_string )
#float (x)
#    if x is a string float, it converts into float
#   also only one string rep of a float
# if x is an integer, it adds 0

# print conversion statements
print()


# 'a_string" + 'b_string" --> a_stringb_string
#   if the operands are strings, + is called concatenation= glues two strings together to get one string
#   GOTCHA: cannot + a number and a string together

print( 'integer_string = \'' + integer_string + '\'' )
print( 'decimal_string = \'' + decimal_string + '\'' )
print( 'decimal_number =', decimal_number )
print( 'integer_number =', integer_number )

print()

print( 'i1 = int( integer_string )' )
print( 'i2 = int( decimal_number )' )

print()

print( 'f1 = float( integer_number )' )
print( 'f2 = float( decimal_string )' )

print()
pause.until_ready()
print()

# use conversions in arithmetic
total1 = i1 + i2 #both i1 and i2 are integers, so the answer is an int
total2 = f1 + f2 #both f1 and f2 are floats, so the answer is a float

# we can take strings and convert them into either types of numbers (int or float) and do arithmetiv
#we can convert

print( 'i1 + i2 =', total1 )
print( 'f1 + f2 =', total2 )

print()
pause.until_ready()
print()

# define and print some numbers for string cast
nbr1 = 14      # integer
nbr2 = 1.5      # decimal

print( 'nbr1 =', nbr1 )
print( 'nbr2 =', nbr2 )

print()

# get and print string conversions
s1 = str( nbr1 ) # s1= '14'
s2 = str( nbr2 ) # s2 = '1.5'

# print conversion statements
print( 's1 = str( nbr1 )' )
print( 's2 = str( nbr2 )' )

print()
pause.until_ready()
print()

# use them
s3 = s1 + s2 #take s1 + s2 ( string concatenation/gluing) into a single string
# s3 = '14' + '1.5' = '141.5'
# glues exactly how string appear

print( 's1 + s2 =', '\'' + s3 + '\'' )
