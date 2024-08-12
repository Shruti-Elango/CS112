
''' Purpose: estimates annual consumption of a commodity 

    Name: Shruti Elango
    Computing ID: se2ezr

    Checker (if any): n/a
'''
# Get input commodity of interest
consume=input('What is something you consume daily?: ')

# Separately get weekday and weekend day consumptions
weekday= input('How much is consumed on a normal weekday?: ')
weekend= input('How much is consumed on a normal weekend day?: ')

# Compute weekly consumption
weekday_consumption= int (weekday)
weekend_consumption= int (weekend)
week_consumption= (weekday_consumption * 5) + (weekend_consumption * 2)

# Compute yearly consumption
year_consumption= int(52 * week_consumption)

# Report yearly consumption
print('You consume', year_consumption, consume, 'per year!')

# Important time constants
WEEKS_PER_YEAR        = 52
WEEK_DAYS_PER_WEEK    =  5
WEEKEND_DAYS_PER_WEEK =  2








