
''' Purpose(s):
        String chrestomathics
        Motivate the need for looping
'''

ADAGE = "Love is all you need"

# prompt and get from user the number of occurrences to be printed

reply = input( "Enter number of lines to be printed: " )

n = int( reply )
# since we want and integer, reply is a string so we cast it to an int

# print the n occurrences of the string of interest
# sometimes there are too many print statements for us to do manually--> need loop

#counting loop repeat something a certian number of time
#range (x,y)
#   x+start
#  y= up to but not including y - stop point
for loop_variable in range(0, n):
        # here we start at 0
        # and we go all the way up to n-1!!!
        # btwn 0 and n-1, thhere are n numbers!!!!
        print( loop_variable, ';', ADAGE)

        # each time through the loop we print the above things n time
        # 1st time : loop_variable = 0
        # 2nd time: loop_variable =1
        #...
        #n_th time: loop_variables = 0-1
        #yes, loop_variable automatically updates every time he for loop restarts
        # loop_variable coule be named anything that makes sense in context
        # you dont need to define loop_variable before the for loop!!
        # dont use loop_variable outside the loop, otherwise you may overrride something
for i in range(0,n):
    print ( ADAGE)
    print()

    #this is not the same as range!!
    # i will just be the values inside ()
    # i=0
    # i=n
    #not a range! must use range(0,n)
    #this loop will only run 2 times, because there are only 2 values inside ()
for i in (0,n):
        print(ADAGE)

    #rande (0, n) == range (0, n) == range (0,n) --> whitespace dont matter * this is a style rule not a syntax rule

    # read for loops mindfully! recognize what you have written not what you meant when debugging
    # use print statments to help when debugging.
...

print ('total=', total)