
''' Implements module tex.py for test 2
'''

def words( s ) :
    word_list = s.split()
    number_of_words = len(word_list)
    return number_of_words
    pass

if ( __name__ == "__main__" ) :

    import run

    run.test_words()
