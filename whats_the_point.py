
''' Purpose: show how to get a number with desired number of significant digits
    after the decimal point.  makes use of round() capabilities.
'''

# get input and convert to decimal
reply = input( "Enter number: " )
number = float( reply )

print()

# round ( x, y )
# x+ the number you want rounded
# y= the number of decimal place you want to round to (optional)
# if not given, will round to an int


# compute eight versions of number
number6 = round( number, 6 )            # rounds to six places after the decimal
number5 = round( number, 5 )            # rounds to five places after the decimal
number4 = round( number, 4 )            # rounds to four places after the decimal
number3 = round( number, 3 )            # rounds to three places after the decimal
number2 = round( number, 2 )            # rounds to two places after the decimal
number1 = round( number, 1 )            # rounds to one place after the decimal
number0 = round( number, 0 )            # rounds to zero places after the decimal
                                        #    -- still produces a float

rounded = round( number    )            # rounds to an integer

# display original number and its eight variants
print( 'number:', number )

print()

print( 'round( number, 6 ):', number6 )
print( 'round( number, 5 ):', number5 )
print( 'round( number, 4 ):', number4 )
print( 'round( number, 3 ):', number3 )
print( 'round( number, 2 ):', number2 )
print( 'round( number, 1 ):', number1 )
print( 'round( number, 0 ):', number0 )

print()

print( 'round( number ):', rounded )
