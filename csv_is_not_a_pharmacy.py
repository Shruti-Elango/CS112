
''' Purpose: practice getting data from a useful dataset
'''

# define the base folder for course csv datasets
CSV_WEB_FOLDER = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/'

import url
#url is the module that prof wrote so we can do more stuff with web contents
# urllib is a pyth

# get name of the dataset
reply = input( 'Enter name of dataset: ' )

print()

# clean up the reply to get file name
file_name = reply.strip()  #we want to clean up the whitespace from the file neame espectially when dealing with web files
# split- makes into a list
#strip cleans up

# get url link for dataset
link = CSV_WEB_FOLDER + file_name

# get the contents of the web file
dataset = url.get_contents( link )

# get_contents() with a csv will give you back as text string --> this will not give you back a dataset
# we want a dataset, use get_dataset()

print( 'dataset' )
print( dataset )
print()

reply = input( 'Enter when ready: ' )

# get dataset from the web
dataset = url.get_dataset( link )
# returns us a list of rows
print(dataset)

#csv = comma seperated values
# it's formatted  info where each row ise seperated by a new line
# like an excel sheet

# divide dataset into header and data
header = dataset[ 0 ] #0th row will contain the headers
data   = dataset[ 1 : ] #from row 1 to the end of the dataset is the rest of the data
# we can do splicing on lists like do with strings
# from here, we can refer to these two different lists as header and data
# header is a list that has names of columns
# data is list of lists/ rows that contain everything else in the dataset

# print the header
print( 'header:' )
print( header )
print()

# print the dataset data
print( 'data:' )
# print out each row in the list of rows data
for row in data :
    print( row )

print()
