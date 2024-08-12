
''' Purpose: reinforce loop mechanics
'''

import pause

# get some sequences
color = input( 'Enter your favorite color: ' )

reply =  input( 'Enter some names: ' )
names = reply.split()

numbers = [ 12, 7, -11, -12, 59 ]

print()

print( 'color =', color )
print( 'names =', names )
print( 'numbers =', numbers )

print()

# one-by-one go through the characters in color
for ch in color:
    up_ch = ch.upper() #ch.upper() --> gets uppercase version of the character ch
    print( up_ch )    #print the uppercase version out

print()

# one-by-one go through the names in names
# for each string name in our list of names
for name in names:
    cap_name = name.capitalize()    # capitalize our name one at a time
    print( cap_name )

print()

# one-by-one go through the numbers in numbers
# for each number in our list numbers
for nbr in numbers:
    comp_nbr = -nbr    #make our number its opposite - negate it == nbr * -1
    print( comp_nbr )

print() ; pause.until_ready() ; print()

# let's build a new string out of the color where the characters are separated
# by blanks
#if we input "turquoise' --> we want a new version = 't u r q u i s e'
spaced_out_color = ''     # our string accumulator always starts as the empty string
# for each character in the string color
for ch in color:
    spaced_out_color = spaced_out_color + ch
    # we concatenate our character to the accumulator
    # and a space after every character
    # '' is just an empty string that has nothing; it is NOT a space

    #ch='t'
    #spaced_out_color = 't'

    #ch= 'u'
    #spaced_out_color ='t u'' ...

    print(spaced_out_color) #indented print statement will print that for ever run of the loop


print() ; pause.until_ready() ; print()

# let's build a list of the number of characters in each one of the names

name_lengths = []
for name in names :
    n = len (name)
    name_lengths.append( n)
    print(name_lengths)
#print( names )


print() ; pause.until_ready() ; print()

# let's find the longest name length
longest_name_length = ...

print( 'longest name length =', longest_name_length )

# let's find the name that occurs first alphabetically
first_alphabetically = ...

print( 'first alphabetically: ', first_alphabetically )
