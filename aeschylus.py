

'''  Name: Shruti Elango
    Computing ID: se2ezr

    Checker (if any): n/a
    Purpose: solve the aeschylus.py homework assignment
'''

# get input text

text = input( 'Enter text: ' )

print()

# convert text into a list of words 
list= text.split()

# print the list of input words
print (list)

# build a new word list whose elements are s-less versions of the input words
list2=[]
for x in list:
    s_less = x.replace('s', '')
    list2.append(s_less)

# print the list of s-less words
print(list2)
