
''' Purpose: considers the subltety of swapping variable values
'''

# get and echo inputs

reply  = input( 'Enter two words: ' )

w1, w2 = reply.split()

print( )
print( 'w1 =', w1 )
print( 'w2 =', w2 )

print()

# swap the values of w1 and w2
#remember_w1 = w1  # we are starting the value of w1 in another variable, so we don't lose it
#w1 = w2     # we update w1 with the value of w2, so the old value of w1 is lost!!
#w2 = w1     # if we update w2 with w1, w1 now has the same value as w2, so same values
#w2 = remember_w1 # remember_w1 holds the original value of w1, this is the value we want to update in w2

# swapping in the print statement does not change the value of the variable! You're just cheating :)

# swapping both at the same time
#when you have 2 things on the left side, yoy muct have 2 things on the right side

w1, w2 = w2, w1
#right side: get the current value of w2 and w1
# left side: put the current value of w2 into w1, put the current value of w1 into w2

# print results

print( 'After swapping' )

print()

print( 'w1 =', w1 )
print( 'w2 =', w2 )

n = 4
n= n + 1
# right side
