
''' Purpose: expand input processing capabilities by splitting
         an input string into its component words
'''

# get input
reply = input( 'What are your three favorite words: ' )
#reply is a single string
#   'a b c' is still a single string, not 'a', 'a', 'c'
print ('reply=', reply)

# sometimes the use might enter spaces in front of and after their input --> we need to clean them up

print()

# a_string.split()
#reply.split() # split reply into a list of things (individual words)
#split() is a string memeber function--> gives you list of things that make up that strong
# split based on spaces: gets rid of spaces- something string have

# determine individual words w1, w2, and w3

w1, w2, w3 = reply.split()      # function need () to run!!!
# if reply = ' you me       us' ---> gives a list that has 'you', 'me', 'us'

#if you input multiple integers, you need to split them into individual strings
# then convert each into an integer one at a time

# display results
# each word on its own line
print( w1 )
print( w2 )
print( w3 )

