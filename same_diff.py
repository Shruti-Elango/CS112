
''' Purpose: further introduce decision making
'''

# get the input
reply = input( "Enter two numbers: " )

# convert the input into integers
m, n= reply.split()
m, n = int(m), int(n)

# compare the numbers to determine their relationship


# display the result
if ( m< 0 and n<0 or m>0 and n>0):
    print ('have same sign')
elif (m>0 and n>0 or m<0 and n<0):
    print('have different signs')
else:
    print('bad input')
# all done
