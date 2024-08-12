
''' Purpose: construct list of n base 2 digits for a user-supplied n
'''

import random # want random values, then we need the random module

# get the number of wanted bits
reply = input( 'How many bits: ' )

n = int( reply )

print()
                                
# create an empty list of bits

bits = []                  # start off with an empty list

# add n random 0/1's to bits
# for each loop we want to generate a bit, which includes values 0 and 1
# then we want to append this new bit into our lists of bits
# n is how many bits we want, got from user
for i in range( 0, n ) :   # i is the iterator

    # each iteration want to add another bit to the list of bits

    # get the next bit

    #strategy 1
    #bit = random.choice([0,1]) #choice() needs lis or string as a sequence

    #strategy 2
    bit= random.randrange(0,2) #also is same as random.randrange(2)

    # append the bit to the list of bits so far

    bits.append( bit )  

# print bits 
print( bits )


