
'''
Purpose: gain experience with if-elif-else
'''

# report message based on day of week
#       Sunday: weekend day
#       Monday: start of school week
#      Tuesday: school day
#    Wednesday: school day
#     Thursday: school day
#       Friday: end of school week
#     Saturday: weekend day

# get day of interest
reply = input( 'Enter day of week: ' )

# put day in standard format - first letter capitalized, others lower case
day = reply.strip()
day = day.capitalize()

# day = reply.strip().capitalize()   # alternatively could also be written as

print( )

# analyze and report on day

# to evaluate multiple expressions, we can use if/elif/else structures
# is it monday, is it tuesday....?
if(day=='Sunday'):
    print('weekend day')
elif (day == 'Monday'):
    print('start of school week')
elif (day == 'Tuesday'):
    print('school day')
elif (day == 'Wednesday'):
    print('school day')
elif (day == 'Thursday'):
    print('school day')
elif (day == 'Friday'):
    print('end of school week')
elif (day == 'Saturday'):
    print('weekend day')
else:
    print ('bad input')

#ORRRRR

if ((day=='sunday') or (day =='saturday')):
   print('weekend day')
elif (day == 'monday'):
    print('start of school week')
elif (day == 'friday'):
    print('end of school week')
elif(day in ["tuesday", "wednesday", ' thursday']):
    print( 'school day')

    # canNOT do day == 'sunday' or 'saturday' --> must do the statements separately
    # still legal but not what you want
    # == is more important than or --> gets evaluated first before the string 'saturday"