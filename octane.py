
''' Purpose: Experience the thrill of random generation and list examination

    Task: Prompt and get three integers s, n, and d from its user (in that
          order). Use integer s as a seed to the Python random number
          generator. Then print n octal digits (base 8 digits) line by
          line by line. Then print the number of generated occurrences of d.
          There should be no other output

    Checker:

'''

# needed module
import random

#  Get the input 

reply = input( 'Enter three numbers: ' )

print()

#  Convert the input into the integers s, d, n   
s, n, d = reply.split()

s, n, d = int( s ), int( n ), int( d )
# s =seed
# n= how many numbers we need to generate
# d = value we're interested in--> need to find how many times this value occurs
# in a list of n octal numbers

# octal numbers = numbers in range 0-7
#  Set the seed for generating random values 
random.seed( s )

# Generate n random octal numbers and store them in a list

# Start by initializing the list holder
octals = []

# One-by-one add n octal numbers to the list holder
for i in range (0, n) :
    digit= random.randrange(0,8) # range is [0,8)
    octals.append(digit)

# Print the list
print( "octal digit list:", octals )

print()

# Determine number of generated octal values equal to d and print
number_of_occurences_of_d_in_octals = octals.count( d )

print( "number of times value", d, "in list:", number_of_occurences_of_d_in_octals )
