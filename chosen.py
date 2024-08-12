
""" Purpose: introduce some another function from module random
"""

# by default the random module produces different interactions everytime we use it

import random # random is another python library that muct be imported

#seed() is a function in random
# pass in anything --> it will set the random machine into a certian state
# so then everytime you run the program it will choose the same randomness
# of the program and regardless of your computer
# kif put nothing there in the function the seed will be the current time so will be randome everytime you run the program
random.seed( )
# seed can be a number ( ints, floats), strings lists etc

# random function choice( seq ) when a given a sequence as a parameter returns
# a random element from the sequence

### get a string and choose four of its characters (repetition allowed)
# this will random choice everytime you run it, diff on each compt.
s = input( "Enter a string: " )
# random.choice( s )--> function in random where you can give it a string, it gives a random character from the string
# each use of the choice function will produce choice for a character within the string s
# 2 random choices may be the same
i1 = random.choice( s )
i2 = random.choice( s )
i3 = random.choice( s )
i4 = random.choice( s )

# if seed is set to random.seed('1112')
# choice will choose a random strinf but it will be the same choice everytime you run the program
# let s= abcdefghij
# so i1 may choose 'j' from s and i2 may choose 'f'
# if seed not set then when you rerun the program
print ()

print( "Four random characters from string", s, ": ", i1, i2, i3, i4 )

print ()

### get a list of words and choose four (repetition allowed)
reply = input( "Enter some words: " )

user_words  = reply.split()
#can also pass in a list into random.choice (list) and it will hand back a random element from the list
w1 = random.choice( user_words )
w2 = random.choice( user_words )
w3 = random.choice( user_words )
w4 = random.choice( user_words )

print( "Four random words from list", user_words, ":",  w1, w2, w3, w4 )

