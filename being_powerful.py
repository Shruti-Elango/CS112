
''' Purpose: demonstrate int and float numeric input processing
'''

# get inputs
x_reply = input( 'Enter base (integer): ' ) #x_reply stores our base int
n_reply = input( 'Enter exponent (decimal): ' ) #n_reply stores our exponent float from user
# BUT REMEMBER, input() gives us back strings!!! NOT numbers!!

#print('type of x_reply is', type( x_reply ) ) #type() is a function that tells what type x is
#print('type of n_reply is', type( n_reply ) )

# convert inputs to numerics
x = int( x_reply )                  # cast string x_reply to get an int
n = float( n_reply )                # cast string n_reply to get a decimal

#int(): x must be an int, float, or a integer numeric string
#   has to be direct conversion
#   if x is a string like '3.8' --> will fail

# compute x to the nth power
value = x ** n
# we have to convert our replied into numeric types (int, float) to do exponentiation
#iotherwise, cannot do this with strings

# display result
print( value )
