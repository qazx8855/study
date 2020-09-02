def select_word_at_random(word_select)->str:
    '''document'''
    if  word_select == 'FIXED' or word_select =='ARBITRARY'  :
        
        return (load_words(word_select)[random_index(load_words(word_select))])
    
    elif word_select =='ARBITRARY':
        return (load_words(word_select)[random_index(load_words(word_select))]) 
    else:
        return None     