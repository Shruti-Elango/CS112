''' Purpose: introductory take on examining a table of values
'''

# define table / dataset
# a table is a list of lists
# each sublist = row
# each row= column/element in that sublist
table = [ ["A", "B", "C" ], [ "D", "E", "F" ], [ "G", "H", "I" ], [ "J", "K", "L", "M" ] ]

# table [0] is a list in itself --> ['A', 'B', 'C']

print( "table:", table )

print()

# determine number of rows in table
# amount of sublists
nrows = len( table )

print( "the table has", nrows, "rows" )

print()

# print each row of the table along withs number of columns
# row is not a keyword, were just calling it row because it represents a sublist in the table
# which we refer to s a "row"
for row in table :
    ncols = len( row )      # since row is a list in iteself, we can use len() to find the number of elements
                            # or number of columns in this row
    print( "row", row, "has", ncols, "columns" )

#1st time : row = ['A', 'B', 'C'} this is a list! can use len to find the number of things (3)
# this number of elements of the sublist is also the number of columns.
print()

# print each row of the table using row indices
# range of indices always starts at 0 and go up to but not including the (length of the list -1)
for r in range( 0, nrows ) :
    row = table[ r ]            # get the current index of the table--> the element at each index is a list/row
    print( "row", r, ":",  row )

