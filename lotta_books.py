
''' Purpose: dataset nuance introduction
'''

# define and print dataset header
# names of our columns for the table- spacing so it aligns with book info beloe
header = [ "Name",                             "Author",           "Language", "Date", "Sales" ]

print( "header:", header )

print()

# determine and print index of names, sales, and date columns of dataset
# here we are determine where certian columns/elements are in a list
# some_list.index( thing_you_want_to_find_in_some_list ) --> gives you the index at which the thing
# first occurs in the list some_list; must exactly match the thing in the ()
# find () is for strings only; use index() for lists
sales_column = header.index( 'Sales' )  # where is 'Sales' in the list header --> give back
name_column  = header.index( 'Name' )  #^
date_column  = header.index( 'Date' )  #^

print( 'sales column:', sales_column )
print( 'name  column:', name_column )
print( 'date  column:', date_column )

# subscript operator [] --> want an INT --> gives you the ELEMENT at that index in the sequence
# index() or find () --> wants the element as an argument --> gives you the INDEX of that element at which
# it first occurs

print()



# define dataset
# each sublist is a book info; each column is each piece of info about the book
# organized so that it matches the scheme/names in the list header
# list can hold multiple types of information: strings, numbers, lists, etc.
books = [
         [ "Alice's Adventures in Wonderland", "Carroll",          "English",  1865,   100000000 ],
         [ "And Then There Were None",         "Christie",         "English",  1939,   100000000 ],
         [ "Dream of the Red Chamber",         "Xueqin",           "Chinese",  1754,   100000000 ],
         [ "Don Quixote",                      "de Cervantes",     "Spanish",  1605,   500000000 ],
         [ "Harry Potter",                     "Rowling",          "English",  1997,   447000000 ],
         [ "The Hobbit",                       "Tolkien",          "English",  1937,   150000000 ],
         [ "The Little Prince",                "de Saint-Exupery", "French",   1943,   150000000 ],
         [ "The Lord of the Rings",            "Tolkien",          "English",  1954,   150000000 ],
         [ "A Tale of Two Cities",             "Dickens",          "English",  1859,   200000000 ],
]

print( "books:", books ) # not pretty bcs all in one line

print()

# print the rows of the dataset
# so each row is on a different line
# for loop helps visually process the dataset structure and information
for row in books :
    print( 'row:', row )

print()

# determine total book sold amongst the top best sellers of all time
total = 0
# for each book in our dataset named books - named book a book b/c it makes sense (could have named it other things)
for book in books :
    sold = book[ sales_column ]   # get the sales column of each book --> get the value of sales
                                # we know whcih column has the sales/number of books sold b/c we've
                                    # determined it above this
    total = total + sold            # add to the total -accumulate

print( 'total sold:', total ) # print the final value of accumulator

print()

# build a list of the book publication dates
# we can use this list of dates wuth the functions min() and max()
# to find the earliest and latest publication date respectively
dates = []  # since we are building a list, start with an empty list
for row in books :
    year = row[ date_column ]   # for each book/row then find the date column which we've determined previously
    dates.append( year )        # append this date to our list accumulator dates

print( 'dates:', dates )

print()

# determine earliest and latest publication date
earliest = min( dates )
latest   = max( dates )

print( 'earliest:', earliest )
print( 'latest  :', latest )

print()

# determine average publication date

date_total   = sum( dates )   # sum(x) is a built in function
                                # pass in a list of numbers as an argument --> returns the sum/total
nbr_of_dates = len( dates )    # get how many dates there are

average_date = date_total // nbr_of_dates

print( 'average date:', average_date )

print()

# determine earliest and latest published books

# to do so need to first find their indices into dates list, those
#     indices correspond to the row indices into books list
row_earliest = dates.index( earliest )
row_latest   = dates.index( latest )

print( 'row with earliest book:', row_earliest )  # what id the index of the earliest date
print( 'row with latest book  :', row_latest )  # what is the index of the latest date
# the indices of these dates match the row of the books they came from

print()

# use those indices to look at corresponding rows into books dataset
# since the dates index match the books ' index
earliest_row = books[ row_earliest ]    # get the book  with the earliest publication date
latest_row   = books[ row_latest ]   # get the book with the latest date

# print those rows
print( 'info on earliest:', earliest_row )
print( 'info on latest:  ', latest_row )

print()

# print just the names of those books
name_column  = header.index( 'Name' )

earliest_name = earliest_row[ name_column ]
latest_name   = latest_row[ name_column ]

print( 'name of earliest:', earliest_name )
print( 'name of latest:  ', latest_name )


