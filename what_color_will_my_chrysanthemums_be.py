
'''
Purpose: introduce decision making
'''

# determine chrysanthemum color given an input soil pH level
#       acidic soil produces pink chrysanthemums
#   non-acidic soil produces blue chrysanthemums

# acidity threshold

ACIDIC_THRESHOLD = 7.0     # samples less than threshold are acidic

# get soil pH level of interst
reply = input( 'Enter soil pH level: ' )

pH = float( reply )

print( )

# analyze and report effect on chrysanthemums
#   if acidic print 'pink';  otherwise print 'blue'

# if statements--> allows us to selective execute certian blocks of code based on some conditions
#if (keyword)
# (logical expression)
#:
# if the (logical expression) is True, then we do what's in the if statement
#if it's False, then we do something else
if(pH < ACIDIC_THRESHOLD):
    print('pink') # if pH is less than 7.0, then we print string pink
else:
    # else statement does NOt need a condition, bcs it assumes the condition of the (logical statement) in if
    print('blue')
    # if pH is not less than 7 or greater than or equal to
# then we do these lines of code- skip 31

# all done


# you can have nested if/else statements within another if/else statements
#can have a loop
#inside a loop, can have more if statemets
# if (something is true):
#     for loop_var == 1:
#            print ('something')
#      else:
#               print('idk')
# else:
#    print('___')
