
''' Name: Shruti Elango
    Computing ID: se2ezr
Purpose: examine a web file and report on it
'''

# get a hold of the local module url for web support
import url

# define repository for text files of interest
TEXT_REPOSITORY = "http://www.cs.virginia.edu/~cs1112/text/"

# input name of web file
file_name = input( "Enter name of web file: " )

# define the link to the web file -- TEXT_REPOSITORY + name of the web file
link = TEXT_REPOSITORY + file_name

# get the text contents of the date file using url function get_contents()
text = url.get_contents( link )

# split text into a list of words
words = text.split()

# input indices of interest
reply = input( "Enter indices of interest: " )

# split indices reply into a list of numeric strings
nstrings = reply.split()
print(nstrings)
# produce a list of numeric indices from the numeric strings
indices = []
for ns in nstrings :
    num_string = int(ns)
    indices.append( num_string)
#print(indices)
# run through the indices and print the associated word from words
for i in indices :
    associated_word= words[i]
    print(associated_word)

