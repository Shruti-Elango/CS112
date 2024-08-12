
''' Implements test 2 module ds.py
'''

import random

def create( nr, nc, k ) :
    listing = []
    for r in range(0,nr):
        row = []
        for c in range(0,nc):
            cell_pair= random.randrange(0,k)
            row.append(cell_pair)
        listing.append(row)

    return listing
    pass

if ( __name__ == "__main__" ) :

    from test2 import test_ds

    test_ds()
