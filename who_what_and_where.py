
''' Purpose: considers how Python stores and keeps track of variables 
'''

# get inputs into proper form (string and integer)

w = input( 'Enter word: ' )

si = input( 'Enter integer: ' )

sd = input( 'Enter decimal: ' )

print()

print( 'w: ', w )
print( 'si: ', si )
print( 'sd: ', sd )

print()

w_type = type( w )        # get the type of w (str, int, float, ....)
w_id   = id( w )            # where in memory is w

si_type = type( si )
si_id   = id( si )

sd_type = type( sd )
sd_id   = id( sd )

# w, si, sd, are all string
# all are stored close together in memory because we declared them next to each other

# display what we found out

print( 'variable w  is', w_type,  'and is at', w_id,  'and when printed displays', w )
print( 'variable si is', si_type, 'and is at', si_id, 'and when printed displays', si )
print( 'variable sd is', sd_type, 'and is at', sd_id, 'and when printed displays', sd )

print()

# let's cast (convert) si and sd respectively into an integer and decimal

i = int( si )   # convert  si into an integer
d = float( sd )  # convert sd into a decimal/float

print( 'i: ', i )
print( 'd: ', d )

print()

i_type = type( i )
i_id   = id( i )

d_type = type( d )
d_id   = id( d )

# when we print in python, it will not print the quotes so numbers and strings look the same
# you cannot know the type just from looking at the output of the print statements

# display what we found out

print( 'variable i is', i_type, 'and is at', i_id, 'and when printed displays', i)
print( 'variable d is', d_type, 'and is at', d_id, 'and when printed displays', d )
