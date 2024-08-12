
''' Name: Shruti Elango

    Email id: se2ezr

    Purpose: get a positive number from the user; i.e., a number greater than zero
        if the user provides a zero or negative number, repeat the process
        until a positive number is gotten. Afterwards, perform a count down from
        the number to 0
'''

count_down = True

while ( count_down == True ) :

    reply = input( 'Enter positive number: ' )
    #spl= reply.split()
    integer = int(reply)
   # print ('reply=', integer)


    if (integer>0) :
        count_down = False

        for i in range(integer+1):
            x=integer-i
            print(x)

#print( reply )
