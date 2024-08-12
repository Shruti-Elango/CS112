
''' Purpose: show a while statement
'''

# set loop decision variable
looking_for_a_yes_or_no = True

while ( looking_for_a_yes_or_no == True ) : # repeat while looking

    # get cleaned up response
    reply = input( 'Enter (yes / no): ' ) # ask for an input while we are still looking
    # want to look for exactly yes or no
    reply = reply.strip()
    reply = reply.lower()
    print ('reply=', reply)

    # check for valid response.
    if ( reply in [ 'yes','no' ] ) :
    #got one
        looking_for_a_yes_or_no = False # set looking variable to false --> while loop will exit
        # if truth condition is not updated it will run forever

print( reply )

