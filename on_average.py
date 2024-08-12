
''' Purpose: examine a list of words
'''

# get text from user
reply = input( 'Enter text: ' )

print()

# split text into words
words = reply.split()
 
# let's see what we got
print( 'Supplied text =', reply )
print( 'words =', words )

print()

# determine number of words= how many words in the list

n = len (words)

# determine total word length

sum_of_word_lengths = 0  # starts at 0
#the len (x) function can take in a string or a list
# x= string --> find the number of characters in x
# x= list --> how many elements are in the list x

for w in words :
    # get current word's length
    # need an assingment statment so we can recall the value later
    current_length= len(w)
print( 'sum_of_word_lengths:', sum_of_word_lengths)
print (w, ':', current_length)  # -> used to check if on the right path

    # add length to the accummulation
    # want length of each word to be part of the total
    # update the accumulator, increase the sum by the current length
sum_of_word_lengths = sum_of_word_lengths + current_length


# determine average

average_word_length = sum_of_word_lengths / n

print( 'Average word length:', average_word_length )

