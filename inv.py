
''' Implements module inv.py for test 2
'''

def erse( d ) :
    #returns a new data set where each thing is the math opposite
    inverse_d = []
    #build dataset row by row
    #look at each row of d for each row, build a new row where values are flipped
    for row in d:
        inverse_row= [] # always starts empty when the list restarts!
        for cell in row:
            inverse_cell = -cell
            inverse_row.append(inverse_cell)
        inverse_d.append(inverse_row)
    return inverse_d
    pass

if ( __name__ == "__main__" ) :

    import run

    run.test_erse()
