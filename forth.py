
''' Purpose: provide simple testing of module go.py
'''

import go

def test_go() :
    ''' Purpose test the four functions that make up go
    '''

    #### Testing ints()
    
    ns1 = " 3 "
    ns2 = "12    11 -63"
    ns3 = "31 415 92 653 5 9"
    ns4 = " "
    
    r1 = go.ints( ns1 )
    r2 = go.ints( ns2 )
    r3 = go.ints( ns3 )
    r4 = go.ints( ns4 )
    
    print( "ints( ns1 ):", r1 )
    print( "ints( ns2 ):", r2 )
    print( "ints( ns3 ):", r3 )
    print( "ints( ns4 ):", r4 )
    
    print()
    
    ### Testing parse_phone_string()
    
    pn1 = "(201) 867-5309"
    pn2 = "636-555-3226"
    pn3 = "212 555 2368 (help line)"
    pn4 = "888.799.9666 (customer service)"
    
    r1 = go.parse_phone_string( pn1 )
    r2 = go.parse_phone_string( pn2 )
    r3 = go.parse_phone_string( pn3 )
    r4 = go.parse_phone_string( pn4 )
    
    print( "parse_phone_string( pn1 ):", r1 )
    print( "parse_phone_string( pn2 ):", r2 )
    print( "parse_phone_string( pn3 ):", r3 )
    print( "parse_phone_string( pn4 ):", r4 )

### run tester if a program
    
if ( __name__ == "__main__" ) :
    test_go()
