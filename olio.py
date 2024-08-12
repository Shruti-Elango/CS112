
''' Purpose: develop programmer-defined functions
'''
#modules do not have codes to execute
# there are just functions that we define
# when you try to run it, there will be no output

# function voting_age(): returns how old you need to be to vote; i.e. the
#     integer 18.

def voting_age():  #does not need parameters because we are not calculating anything
    # just returns number 18
    #indent for body of function
    result= 18

    # return is a keyword--> indicates what value to retunr from the function
    # once retunr is executed, the function finishes
    return result   #result = 18 so return 18

    # any code below return will not be executed

# function has_blanks( s ): returns a whether s contains at least one blank
#     character; i.e., returns True if s contains a blank, and returns
#     False otherwise.

def has_blanks (s):
    '''
        Function takes in one parameter, s, where s is a string
        returns True or False depending on whether s has at least one blank or not

    '''
    if(' ' in s):
        result= True
    else:
        result= False

    return result

# function great_seal( ): prints the string 'E Pluribus Unum'

def great_seal():
    '''
    Takes in no parameters. only prints the string 'E Pluribus Unum'
    Does not return anything! ---> will hand back keyword none
    '''
    print('E Pluribus Unum')

# function a_ing( n ) prints n lines of output. The first line prints a
#     single 'a', the second line prints 'aa', the third line prints 'aaa',
#     and so on.

def a_ing( n ):
    '''

    Takes in 1 parameter, n, where n is an int
    Prints 1-> n 'a' per line n times
    '''
    output_line= ''
    for i in range (0, n):
        # for each i, add one more 'a' to the string
        output_line = output_line + 'a'
        print (output_line)