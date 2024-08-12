
''' Purpose: consider string casing functions
'''

text = input( "Enter text: " )

substring = input( "Enter substring: " )

i = input( "Enter index: " )
i = int( i )

print()

# count occurrences of text
total = text.count( substring )
# count (x) needs at least one argument --> looks for x inside the string and counts how many times x occurs
# matches exactly- case matters!

from_index_i_on = text.count( substring, i )
# count() takes an optional second argument = count (x,y)
# y is the place you should start looking in the string, like from place 1 or 2 or 3 etc.
# includes y and then to the end of the string

print( "text.count( substring ) =", total, "       # count all" )
print( "text.count( substring,", i, ") =", from_index_i_on, "    # count starting from index", i )
# spaces inside a string is a character--> counts towards the length and can be used with the count() function
# metaphysical; in front/after each character is an empty string--> counts that
# kinda weird; not something that practically used.


# parameter: things that define the arguments for each function--> tells the function what to expect when you use it
# count(x) --> is our parameter that tells the count() function to expect at least one argument