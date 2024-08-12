
'''Name: Shruti Elango
    Computing ID: se2ezr

    Checker (if any): n/a
Purpose: practice getting web content into a useful dataset and using then dataset
'''

import url

# helpful constant
CSV_BASE_FOLDER = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/'

# specify data source
reply = input( 'Enter the name of a data set: ' )

name = reply.strip()

# set link
link = CSV_BASE_FOLDER + name

# get dataset from data source
dataset = url.get_dataset( link )

# process the dataset row-by-row
mins = []
for r in dataset :
    min_value= min(r)
    max_value= max(r)
    print(min_value, max_value)
