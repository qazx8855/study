
from a1_support import *

def compute_value_for_guess(word,start_index,end_index,guess)-> int:
    
    scores = 0
    right_guess = word[start_index:end_index+1]  
    print (right_guess) #test

    for i in range(0,len(right_guess)):
        
        if guess[i] == right_guess[i]:
            if guess[i] in VOWELS:
                scores += 14
            
            elif guess[i] in CONSONANTS:
                scores += 12
        
        elif guess[i] in right_guess and guess[i] != right_guess[i] :
                scores += 5
    
    print (scores) #test
    return scores


            

            



compute_value_for_guess('crusing',0,2,'rcu')

