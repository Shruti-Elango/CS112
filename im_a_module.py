
''' Purpose: help introduce tester statement if ( __name__ == '__main__' )
'''

def f() :
    ''' Purpose: be a function
    '''

    return 1112

'''
# test function f()
# we can invoke/use the function we've defined in the same modeule
result = f()
print( 'testing result:', result )
'''

# testing within a "main" block
# runs every time we import im_a_module ( this file - so run im_a_module)
#then we ivoke the f() function
# dont worry about this too much, it'll be written for you
if ( __name__ == '__main__' ):    # __name__ is a built in python variable.
    print("__name__=", __name__)
    import im_a_tester_program    #   it is set to the string '__main__' if
                                  #       you are running the file as a program
                                  #   it is set to the name of the file if
                                  #       the file is being imported

else:
    print("__name__=", __name__)
