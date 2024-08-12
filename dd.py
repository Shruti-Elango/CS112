
''' Implements test 2 module dd.py
'''

def iso( d1, d2 ) :
    dictionary_keys = d1.keys()
    keys_list = list(dictionary_keys)
    dic_key2 = d2.keys()
    keys_list2= list(dic_key2)
    absd= keys_list.split()
    cond= keys_list2.split()
    if absd in cond:
        return True
    elif cond in absd:
        return True
    else:
        return False


    pass

if ( __name__ == "__main__" ) :

    from test2 import test_dd

    test_dd()
