
''' Purpose: demonstrate string acquisition (the getting of input)
'''

# get input

reply = input( 'Please provide text: ' )
#input() is a build-in function; no import needed
# its argument (something inside())= instructions to the user- string
#leave space after colon
#pauses the program until user types something and then hit the enter key
# converts input into a STRING ALWAYS---> stores it into the variable reply
print( 'Your reply was: ', reply ) #reply has the string version of whatever you typed

print()

# get more input

reply = input( 'Please provide more text: ' )

print( 'Your new reply was:', reply )

