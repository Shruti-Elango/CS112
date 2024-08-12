
'''Name: Shruti Elango
    Computing ID: se2ezr

    Checker (if any): n/a
purpose: use random, str, and list to generate a random sentence based on
        user input.  the sentence is of form
            adjective noun verb adjective noun
'''

# needed modules
import random

#####  steps for random sentence generation

# Prompt for a word and use the word as the seed for random generation.
reply1 = input( "Enter seed: " )
value = reply1.strip()

random.seed( value )

# Prompt for adjectives and create a list of adjectives by splitting up the
# user reply.
reply2 = input( "Enter adjectives: " )
adject = reply2.split()

# Prompt for nouns and create a list of nouns by splitting up the user reply.

reply3= input ('Enter nouns: ')
nouns= reply3.split()

# Prompt for verbs and create a list of verbs by splitting up the user reply.

reply4 = input ('Enter verbs: ')
verbs = reply4.split()

# Use the random module choice() capability to generate a sentence of form
#       w1 w2 w3 w4 w5
# where 
#       w1 is a random adjective,
#       w2 is a random noun,
#       w3 is a random verb,
#       w4 is a random adjective, and
#       w5 is a random noun.
# and where the parts of the sentence are randomly generated in that order,
# that is, w1 then w2 then w3 then w4 and lastly w5.

w1 = random.choice( adject )
w2 = random.choice( nouns )
w3 = random.choice( verbs)
w4 = random.choice( adject )
w5 = random.choice( nouns)

# Print sentence w1 w2 w3 w4 w5

print( w1, w2, w3, w4, w5 )
