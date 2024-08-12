
''' Purpose: determine a rough estimate of the geocenter of the
        continental USA
'''

# get access to web-based data support
import url

# specify dataset web location
CSV_WEB_FOLDER = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/'

# dataset name
CONTINENTAL_DATASET = 'usa-continental.csv'

# set link
link    = CSV_WEB_FOLDER + CONTINENTAL_DATASET

# get the dataset of interest
locations = url.get_dataset( link )

# determine geocenter

# a loop that might be helpful for solving the problem
#strategy 1
latitudes = []
longitudes = []
for location in locations :
    town, state, latitude, longitude = location

    latitudes.append(latitude)
    longitudes.append(longitude)

#print (latitudes)
#print(longitudes)

min_lat = min(latitudes)
min_long = min (longitudes)

max_lat = max(latitude)
max_long = max(longitude)

min_max_lat_avg = (min_lat + max_lat) / 2
min_max_long_avg = (min_long + max_long) / 2
print(min_max_lat_avg, min_max_long_avg)