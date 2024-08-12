
'''
Author: Shruti Elango
Purpose: introduce decision making
Email ID: se2ezr
'''

# get the input
reply = input( "Enter two numbers: " )

# convert the input into integers
m, n= reply.split()
m, n = int(m), int(n)

# compare the numbers to determine their relationship
# display the result
if ( m == n ):
    print ('equal to')
elif(m < n):
    print('less than')
elif (m>n):
    print('greater than')
else:
    print('bad input')

# all done
