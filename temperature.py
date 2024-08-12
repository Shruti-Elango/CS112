
''' Purpose: relate a cautionary tale -- make sure your expressions do
        what they are supposed to do
'''

# get Celsius temperature c

reply = input( 'Enter Celsius temperature: ' )# always hands back a string

c = int( reply ) # convert string numberinto an int

print( )

# formula for f = 9/5 c + 32
# python uses PEMDAS

# compute respectively, f1 and f2, the decimal and integer Fahrenheit equivalents of c 

f1 = 9/5 * c + 32
f1 = round (f1, 1 )
# itll round to the nearest integer

# cannot have implicit multiplication, MUST USE * to indicate multiplication
# 3c --> not ok
# 3* c--> ok

# want integer answer
# why 9//5 * c + 32 gives wrong answer rn?
# 9//5 --> 1 because drops the decimal
# --> 1*c + 32 = 56 # a GOTCHA

f2 = 9 * c // 5 + 32 # double slash= integer division
# f2 = 9 * c // 5 + 32 works- when doing divison make the numerator as big as possible to divide--> more accurate answer
# can also use int()

f2 = int(f1) # we have the decimal version in f1 and then fidning integer version to drop the decimal places
# use round
f2 = round (f1)
# display results

print( c, 'C =', f1, 'F' )

print( )

print( c, 'C =', f2, 'F' )
