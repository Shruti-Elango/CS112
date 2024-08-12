
''' Name: Shruti Elango
    Computing id: se2ezr

    Purpose: determine the worth of a piggy bank

    Problem statement:
        Prompt user respectively for four values: a number of quarters,
        dimes, nickels, and pennies.  Then compute and display how much the
        indicated coins are worth.
'''

### get the coinage of interest
reply = input( "Number of quarters, dimes, nickels, and pennies: " )


### convert input into integers
q, d, n, p = reply.split()
quarters= int(q)
dimes= int(d)
nickels= int(n)
pennies= int(p)

### compute worth
q_worth= .25*quarters
d_worth= .10*dimes
n_worth= .05*nickels
p_worth= .01*pennies
total_worth= q_worth + d_worth + n_worth + p_worth
final_worth=round(total_worth, 2)

### print worth
print('Coinage')
print()
print(q, 'quarters')
print(d, 'dimes')
print(n, 'nickels')
print(p, 'pennies')
print()
print('Are worth', final_worth, 'dollars!')
