
''' Purpose: convert an input list of integers into an integer list
'''

# get input
reply = input( 'Enter integers: ' )

print()

# split reply into list of numeric strings
nbr_strings = reply.split()

#  see what we got
print( 'nbr_strings:', nbr_strings )

print()

# convert numeric text into list of numbers
#list accumulator
# set up the accumulator to prepare for adding elements
numbers = [] # list accumuation always start with on empty list; denoted by [] brakets

# process the strings of nbr_strings one-by-one
# for each numeric string (ns) in our list of numeric strings
# we want to cast each numeric string on it integer counterpart
for ns in nbr_strings :
    # process the current numeric string

    # get numeric equivalent of ns
    nbr = int(ns)
    print(nbr)

    # add equivalent to list of numbers
    # put nbr into our list accumulator, add to the end of a list
    # adding elements at the end of a list is called appreding --> we use the function append(x)
    # where x is something you want to put at the end of the list
    numbers.append(nbr) # format: your_list.append(nbr) --> we have put nbr to the end of our list called numbers

# append() will change the original list --> you don't need an assignment statement
# append does not hand anything back it modifys the list.
    # print the updated list of numbers
    print( 'numbers:', numbers )
 




