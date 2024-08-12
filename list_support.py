
''' Support your understanding of lists
        built-in support

'''


# get some lists

print()

s = "we are in it together"

values = [ ]

stuff  = [ 'abc', 1112, 2.71, ]  #lists can have mulitple diff vales- multiple types

digits = [ 3, 1, 4, 1, 5, 9, 2, 6 ]

words  = s.split()         #s.split() --> split our strings on whitespace --> list of words

# determine their sizes



vlen   = len( values )   #length.... so far we have 0 things in the list values

slen   = len( stuff )    # we have 3 things in stuff

dlen   = len( digits )      # we have 8 things in digits

wlen   = len( words )      # we have 5 things in wor

# report their sizes

print( "size of", values, "=", vlen )
print()

print( "size of", stuff, "=", slen )
print()

print( "size of", digits, "=", dlen )
print()

print( "size of", words, "=", wlen )
print()

input()

# determine the max and min of the homogeneous lists

# never have a varibel called max, min, or sum! these are funtion names in pythen
dmax = max( digits )     # max () is a built- in function
dmin = min( digits )      # min(x): # gives you back the min value within x
# lexicographical order: ordering by the value of each character in the alphabet
# a is the min value and z is the max value
# when max() and min() compares btwen string, they compare EACH CHARCATER AT A TIME
# 'we' vs 'are'
# compares 'w' vs 'a'
wmax = max( words )
wmin = min( words )

print( "max of", digits, "=", dmax )
print( "min of", digits, "=", dmin )
print()

print( "max of", words, "=", wmax )
print( "min of", words, "=", wmin )
print()

s_max =  max(stuff)
print(s_max)
# if your list has both number and strings, max() cannot compare btwn strings and number!!
# only use max()
