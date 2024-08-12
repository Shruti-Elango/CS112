
''' Purpose: demonstrate while loop and dict mappings
'''

# get url reading abilities
import url

# where is the commodity cost mappings
COMMODITIES_CSV = 'http://www.cs.virginia.edu/~cs1112/datasets/csv/spot-prices.csv'

# get web-based commodities dictionary
commodity_mappings = url.get_dictionary( COMMODITIES_CSV )

# while user is supplying queries, process them. user indicates no more
# queries by not entering an empty response

still_looking_for_queries = True

while (still_looking_for_queries == True ) :
    # prompt for next query
    reply = input( "Enter commodity: " )

    # clean up response to
    reply = reply.strip()
    query = reply.lower()

    # examine query -- there are three possibilities
    #   is empty => done looking for queries
    #   is in dictionary => process request
    #   is not in dictionary => flag that request is unknown.

    if (query in commodity_mappings):
        output_word= commodity_mappings.get(query)
        print(output_word)
    elif (reply == ''):
        still_looking_for_queries = False
    elif (query not in commodity_mappings):
        print('pricing unknown')


# all done
