
''' Purpose: stepping stone to nested looping
'''

# get n
reply = input( 'Enter number of columns: ' )
n = int( reply )

# performed repeated printing of a number series
#    print a line of the form row: 0 1 2 ... n-1

#    to do so need to first print the row: part
#    then on same line print out the values 0 1 2 ... n-1 one after the other

# end=' .. ' in the print statement is an optional parameter--> thats printastic
print('row :', end=' ') # we want to print row: only once, and then the rest of the numbers
                        # on the same line

# need a for range loop to print each number from 0 to n-1
# c for column
for c in range( 0, n):
    print(c, end= ' ') # we want each number to be printed on the same line but seperated by a space

print() #prints nothing--> ends current line so print statement will print on new line

print('all done')