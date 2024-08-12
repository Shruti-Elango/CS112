
''' Purpose: demonstrate the printing of a list of words, one word per line
'''

# get list of words
reply = input( "Enter several words: " )

words = reply.split()     #splkit reply into a list of words
print =('words=', words)

### print the words word by word
# we dont know how may words there are ---> loop

# here our sequence is a LIST of words [ 'word1', 'word2']
# so loop_variabel will represent each WORD, NOT each character
for w in words:
    # wis the current word; will go through each word inside the list of words
    #1st time: w= 'word1'
    print(w)

...

