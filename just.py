
''' Implements module just.py for test 2
'''

def one( w, x, y, z ) :
    list_values= [w,x,y,z]
    occurences = list_values.count(True)
    if (occurences == 1):
       return True
    else:
       return False
if ( __name__ == "__main__" ) :

    import run

    run.test_one()
