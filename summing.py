
''' Purpose: introduce summing accumulation
'''

# get a list of numbers
reply   = input( 'Enter a list of numbers: ' )
slist   = reply.split()

print()
print('slist=', slist)
print()
 
# convert numeric text into numbers one by one
nlist = []  # initialize holder to prepare for adding elements

for s in slist :
    nbr = int( s )   # cast the numeric string into the type int
    nlist.append( nbr )
    print('nlist=', nlist)

# by accumulation get the sum of the numbers
total = 0

for nbr in nlist :
    total = total + nbr    # add to our running total

# print summation
print( "sum(", nlist, "):", total )
