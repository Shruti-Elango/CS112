
'''Name: Shruti Elango
Computing id: se2ezr
Purpose: determine the number of vowels in user-specified text
'''

# HELPFUL CONSTANT

VOWELS = 'aeiou'

# get the input
text = input( 'Enter text: ' )

# get a cleaned up version (canonical) of the text -- get a stripped,
# lower case version
lower_case=text.lower()

a= str('a')
e=str('e')
i=str('i')
o=str('o')
u=str('u')

# determine and report the number of occurrences of each vowel
vowel_a= lower_case.count(a)
vowel_e= lower_case.count(e)
vowel_i= lower_case.count(i)
vowel_o= lower_case.count(o)
vowel_u= lower_case.count(u)

print()
print('a:',vowel_a )
print('e:', vowel_e)
print('i:', vowel_i)
print('o:', vowel_o)
print('u:', vowel_u)
...
