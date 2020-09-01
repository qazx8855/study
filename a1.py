"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Yuliang_Liu}} ({{s4564914}})"
__email__ = "yuliang.liu@uqconnect.edu.au"
__date__ = "01/09/2020"



# Write your code here (i.e. functions)

def select_word_at_random(word_select)->str:
    '''document'''
    if  word_select == 'FIXED':
        return (load_words(word_select)[random_index(word_select)])
    
    elif word_select !='ARBITRARY':
        return (load_words(word_select)[random_index(word_select)]) 
    else:
        return None      

def create_guess_line(guess_no,word_length)->str:
    '''document'''

    (start,end)=GUESS_INDEX_TUPLE[word_length-6][guess_no-1]

    line='Guess '
    line+=str(guess_no)
    

    for i in range(0, start):
        line += '| - '

    for i in range(start,end+1):
        line +='| * '

    for i in range(end+1,word_length):
        
        line +='| - '

    line +='|'
    return line

def display_guess_matrix(guess_no,word_length,scores) ->None:
    '''document'''

    top_line = '       '
    
    for i in range(1,word_length+1):
        top_line += '| '
        top_line += str(i)
        top_line += ' '
    
    top_line += '|'

    dividing_line = WALL_HORIZONTAL * (9 + 4 * word_length)

    print(top_line)
    print(dividing_line)

    if guess_no == 1:
        guess_line = create_guess_line(guess_no,word_length)
        print(guess_line)
        print(dividing_line)

    elif guess_no > 1 :
        for i in range(1 , guess_no+1):
            if i< guess_no :
                guess_line = create_guess_line(i,word_length)
                guess_line += '   '
                guess_line += str(scores[i-1])
                guess_line += ' Points'

                print(guess_line)
                print(dividing_line)

            elif i == guess_no :
                guess_line = create_guess_line(guess_no,word_length)
                print(guess_line)
                print(dividing_line)

def compute_value_for_guess(word,start_index,end_index,guess)-> int:
    '''document'''

    scores = 0
    right_guess = word[start_index:end_index+1]  
    
    for i in range(0,len(right_guess)):
        
        if guess[i] == right_guess[i]:
            if guess[i] in VOWELS:
                scores += 14
            
            elif guess[i] in CONSONANTS:
                scores += 12
        
        elif guess[i] in right_guess and guess[i] != right_guess[i] :
                scores += 5
    
    return scores


def main()->None:
    """
    Handles top-level interaction with user.
    """
    # Write the code for your main function here

    print (WELCOME)

    while True:
        select=input(INPUT_ACTION)

        if select not in ('s','h','q'):
            print(INVALID)
        elif select == 'h':
            print(HELP)

        elif select =='q':
            break 

        elif select == 's':
            while True:
                word_select = input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
                word = select_word_at_random(word_select)
                
                if word != None: 
                    print('Now try and guess the word, step by step!!')
                
                    word_length = len(word)
                    scores = ()

                    for guess_no in range(1,len(word)+1):
        
                        display_guess_matrix (guess_no,word_length,scores)
        
                        Now_enter_Guess = 'Now enter Guess '
                        Now_enter_Guess += str(guess_no)
                        Now_enter_Guess += ': '
        
                        start_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]
                        end_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]
                        right_guess_len = end_index - start_index  + 1

                        while True:
                            guess = input(Now_enter_Guess)
            
                            if len(guess) == right_guess_len:
                                break
    
                        Score_for_round = compute_value_for_guess(word,start_index,end_index,guess)
                        Score_for_round_tutle = (Score_for_round,)
                        scores += Score_for_round_tutle

                        if guess_no == len(word):
                            whole_guess = guess

                    if whole_guess == word :
                        print ('You have guessed the word correctly. Congratulations.')

                    elif whole_guess != word :
                        print ('Your guess was wrong. The correct word was "%s"' % (word))
                    break
                
        
    



if __name__ == "__main__":
	main()