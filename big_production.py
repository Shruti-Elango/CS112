
'''
Author: Shruti Elango
    Email id: se2ezr

    Purpose: practice interactive program development

    Checker / assistance computing id: NOT REQUIRED
'''

# get the input
reply = input( 'Enter list of integers: ' )

# split reply into a list of numeric strings
split=reply.split()

# print the list of numeric strings
print(split)

# using a list accumulator loop, take the numeric strings one-by-one and
# accumulate a list of integers by appending integer equivalent of each
# numeric string to the list of integers.
nlist = []
for s in split :
    nbr = int( s )   # cast the numeric string into the type int
    nlist.append( nbr )

# print the list of integers
print(nlist)

# Using a product accumulator loop, process the integers one-by-one.
# For each of the integers, update the accumulator by scaling it by
# the integer.
total = 1

for nbr in nlist :
    total = total * nbr

# print the product
print(total)
