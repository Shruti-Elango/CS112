
''' Purpose: Exercise module olio
'''

import olio  #get the olio module by importing it to use functions in olio

# uncomment below lines to test voting_age()
# from the module olio, get the function voting_age
# voting_age() does not have any parameters so when we invoke it, we don't need to pass in an argument
# will always hand back (return) 18 bcs we defined it that way

x = olio.voting_age()
y = olio.voting_age()

print( x )
print( y )

print()

# uncomment below lines to test has_blanks()

line1 = input( 'Enter text: ' )
line2 = input( 'Enter text: ' )

b1 = olio.has_blanks( line1 )
b2 = olio.has_blanks( line2 )

print( b1 )
print( b2 )

print()

# uncomment below lines to test great_seal()

olio.great_seal()
olio.great_seal()

print()

# uncomment below lines to test a_ing()

reply1   = input( 'Enter integer: ' )
reply2   = input( 'Enter integer: ' )
reply3   = input( 'Enter integer: ' )

nbr1 = int( reply1 )
nbr2 = int( reply2 )
nbr3 = int( reply3 )

olio.a_ing( nbr1 )
print()

olio.a_ing( nbr2 )
print()

olio.a_ing( nbr3 )
print()

# a_ing() does not return anything but it defaults to none
# if we assign the retrun value to a variable, then print it out
#that varible will hold None.
result = olio.a_ing(nbr3)
print(result)