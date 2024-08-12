
''' Purpose: get an input code phrase and list of indices. Determine the
             hidden message by using the indices to peek into the code phrase
'''

# get the code phrase that contains hidden message
reply = input( "Enter code phrase: " )

print()

# clean up reply to get code phrase with no leading or trailing whitespace
code_phrase = reply.strip()    #strip() removes leading and trailing whitespaces
# case doesnt matter in this case

# print the code phrase
print( "Code phrase=", code_phrase )

print()

# get the list of indices (as string) for peeking into code phrase
reply = input( "Enter indices for looking into code phrase: " )

print()

# convert reply into a list of numeric strings
numeric_strings = reply.split()         #

# build one-by-one the list of indices out of the numeric strings 
# build a list of integers from the list of numeric strings
indices = []  #list accumulator, starts with empty list

# for each numeric string in numeric_strings, convert to an int and put it into the list indices
# (use i for ints for range stuff, generally - just a convention)
for s in numeric_strings:
    index =int(s)   #s= numeric string --> int(s) --> convert to int version
    indices.append(index)       # remember, you don't have to assign indices = indices.append (index)
                                # append() will update the original list --> puts index at the end of list indices

#we must convert our numeric string into ints bcs indices will only take INTS!
# no strings nor floats

# print the list of indices
print( "Indices:", indices )

print()

# build secret message (string) by peeking into code phrase using the
# indices one-by-one
message = '' #string accumulator starts with empty string as we build from scratch

# we need to peak in the original message at the indices we said to look at
# for each index in the list indices, we look into the original message (code_phrase) at that index
for i in indices:
    ch = code_phrase [i]    # string indices ALWAYS USE BRACKETS [] NOT ()
    #print (i, ch)
    message= message + ch # each time through take the current message and then glue on the nect character ---> update it
# append() is only for lists not strings!!!!
# print secret message
print( "Secret message:", message )
