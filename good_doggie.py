
''' Purpose: demonstrate dict mappings
'''

# get access to url support
import url

# where is the dog to notoriety mappings
PUPPIES_CSV = "http://www.cs.virginia.edu/~cs1112/datasets/csv/puppies.csv"

# get data set
dataset = url.get_dataset( PUPPIES_CSV )

# convert dataset to a form suitable for querying
notoriety = { } #empty dict-- comes with all fucntions

for row in dataset: # for each row in the dataset
    # each row has dogs name adn its importance

    name, importance = row
    name = row[0]
    importance = row[1]
    notoriety[ name ] = importance
    print (notoriety)

# ask for dog of interest
reply = input( "Enter name of dog: " )

dog = reply.strip()
dog = dog.capitalize()

# look up claim to fame
fame = notoriety.get( dog ) # get is the function
# get (key) --> if key is not in dict then it returns the keyword none
#fame2= notoriety[dog]
print( fame )
#print(fame2)
