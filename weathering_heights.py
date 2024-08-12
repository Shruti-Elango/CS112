
''' Purpose: provide weather forecast by accessing US Weather Service web service

    Usage:   user provides a zipcode

    Output:  current forecast for that zipcode
'''

# get url access capability from cs 1112 module
import url 

# define weather.gov base query
# https - s = secure website
WEATHER_GOV_QUERY = "https://forecast.weather.gov/zipcity.php?inputstring="

# forecast delimiters -- these will help us locate where the forcast is -- between the front_delimiter
# and end_delimiter
FRONT_DELIMITER = "<div class=\"col-sm-10 forecast-text\">"   # text that precedes forecast
REAR_DELIMITER  = "</div>"                                    # text that follows forecast

# delimiter lengths
LENGTH_FRONT_DELIMITER = len( FRONT_DELIMITER )    #we need the length of the front delimiter
                                                    #b/c the forecast starts RIGHT AFTER the front_delimiter
                                                    # not where the front_delimiter starts
LENGTH_REAR_DELIMITER  = len( REAR_DELIMITER )

# get zipcode of interest
reply = input( "Enter zipcode: " )
zipcode = reply.strip()                         # clean-up response: clean whitespace

# specify complete query
query_link = WEATHER_GOV_QUERY + zipcode        # get complete link to web


# get response from weather.gov
page = url.get_contents( query_link )  # get_contents() is a function within the url module
                                        # gives it a string that is a link for a website
                                        # then gives back the content of website
#print (page)

# to get the forecast, we need to find it within the page

# start by finding the forecast delimiters
front_index = page.find( FRONT_DELIMITER)       # at what index does the FRONT_DELIMITER start in the string page?
                                                # for strings, we use find() to get the index of the argument
rear_index  = page.find(REAR_DELIMITER, front_index) #Find index at end delim starts
# find the index at which the END_DELIMITER starts
#2nd parameter - find reardelim starting from the front index

#print( front_index, rear_index )

# (mis)try to use those index delimiters to pick off the forecast

forecast = page[ front_index + LENGTH_REAR_DELIMITER: rear_index ] #Includes from front_index an up to but no incuding rear_index
# but if we start at front_index, we also include the FRONT_DELIM string -->
#

print( forecast )

print()

# get the indices for the front and rear of the forecast
forecast_start = front_index + LENGTH_FRONT_DELIMITER

forecast_rear = rear_index

# ready to get and print the forecast
forecast = page[ forecast_start : forecast_rear ]

# print the forecast
print( forecast )
