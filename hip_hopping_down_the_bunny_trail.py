
''' Purpose: deepen variable manipulation understanding.

    Problem: track the number of rabbits over five generations, where
             the number of rabbits doubles each generation. at the start
             there are two rabbits
'''

# first generation
generation  = 1
nbr_rabbits = 2
print('Memory box for generation', id(generation))
#id() is a function, gives the location in your computer of the value of the variable (generation)
print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )

reply = input( 'Enter when ready: ' )           # waits until user enters something

# next generation
generation  = generation+1 # gen is on the right of the old value
nbr_rabbits = nbr_rabbits*2 #double number of rabbits from last gen (2 gen*2 rabbits)
#updating variables- from here on out the gen and nbr_rabbits will have new values unless we update them again
print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )

reply = input( 'Enter when ready: ' )           # waits until user enters something

# next generation
generation  = 3
nbr_rabbits = 8

print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )

reply = input( 'Enter when ready: ' )           # waits until user enters something

# next generation
generation  = generation +1
nbr_rabbits = nbr_rabbits*2

print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )

reply = input( 'Enter when ready: ' )           # waits until user enters something

# next generation
generation  = 5
nbr_rabbits = 32

print( 'Generation: ', generation  )
print( 'Rabbits:    ', nbr_rabbits )
# variables can be re-used and updated

#what happens when there are bigger generations? Let the computer double instead of doing it manually

