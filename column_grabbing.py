
''' Purpose: introductory take on examining a table of values
'''

# define table
table = [ ['A', 'B', 'C' ], [ 'D', 'E', 'F' ], [ 'G', 'H', 'I' ], [ 'J', 'K', 'L', 'M' ] ]

print( 'table =', table )

print()

# print a requested column as a list
# Column= an index into a row
reply = input( "Enter column of interest: " )

c = int( reply )

# need to accumulate the cells in the column c
# A list of things in column c
column = [] # accumulate- start with empty brackets

# for each row in our table
for row in table :
    n= len(row)
    c= n - 1  # c is now the last index in a row since n is the length of the current row
                #we've ignored what we inputted for c before
    # get cell in column c of the row
    #since a column is some element in each row
    #print(row)
    # row is a list  --> we can access individual element in a list similar to how we do it for string
    # we call it subscripting --> find cth element in each list row --> us [] operator
    cell = row[c] # get the thing in column c (cth element) in the list row

    # add the cell to the column list
    column.append(cell)
    
    print( 'row', row, ': column', c, 'cell:', cell )

    print()

    print( 'Column', c, ':', column )

    print ('----------------------')
    print()
'''
[
    ['A', 'B', 'C'] -- this is a row
    ['D', 'E', 'F'] --- this is another row
]

a column from this table is ['A']
                            ['D']
this is the 0th column in the table
the 0th column is at the 0th index of Each row!

If a row has more columns than other rows, and you attempt to access that index
                            
                             

'''