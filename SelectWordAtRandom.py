from a1_support import *

def select_word_at_random(word_select)->str:
    '''document'''
    if not word_select == 'FIXED' or word_select =='ARBITRARY':
        return None
    else:
        return (load_words(word_select)[random_index(word_select)]) 

word = select_word_at_random('FIXED')
print(word)