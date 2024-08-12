
'''
Purpose: stepping stone to nested looping
'''

# get number of rows and columns
reply = input( 'Number of rows and columns: ' )

srows, scols = reply.split()
# we need to convert into ints here because input() return string!
nrows = int( srows )
ncols = int( scols )

# nested for loops! REVIEW THIS
# you can have a loop in another for loop
# produce nrows rows of output
#    for each row produce ncols columns of output
#           row r's c-th output, is value of r + c

# for each row in the range 0 (inclusive) to nrows(exlusive)
for r in range (0, nrows):
    print ('row', r, ':')
    # for each row, we process EACH COLUMN
    # this inner for loop will run to completion before the outer for loop starts on its next iteration
    # then this inner for loop will run to completion again for the next outer loop
    # and so on until the outer for loop finishes!
    for c in range (0, ncols):
         #print ('    ', c, end='  ')        # if we add end= then we print each column number on the same line for each row

            # print() # end the current line then so the next row will print on a new line
         # determine cell value for column c
         cell = r + c
         # print cell value
         print( cell, end="\t" )
    print()
