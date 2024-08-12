
''' Purpose: help introduce tester statement if ( __name__ == '__main__' )
'''

import im_a_module

def test_im_a_module() :

    result = im_a_module.f() #use function f() from module
    # if we invoked f() in the im_a_module (line 12-15)--> we will end up with another line of "1112"

    print( "im_a_module.f():", result ) # print result

# invoke the function in the program called test_im_a_module()
test_im_a_module()
