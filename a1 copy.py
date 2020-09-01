"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{user.name}} ({{user.id}})"
__email__ = ""
__date__ = ""



# Write your code here (i.e. functions)

def select_word_at_random()->str:
    #document
    while True:
        word_select=input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
        word_list=()
        if word_select =='FIXED':
            word_list=load_words('FIXED')
            break
            
        elif word_select =='ARBITRARY':    
            word_list=load_words('ARBITRARY')
            break

    number = random_index(word_list)

    word = word_list[number]   
    return (word)       

def create_guess_line(guess_no,word_length)->str:
    #document
    line='Guess '
    guess_no_str=str(guess_no)

    (start,end)=GUESS_INDEX_TUPLE[word_length-6][guess_no-1]
    line+=guess_no_str

    for i in range(0, start):

        line += '| - '

    for i in range(start,end+1):

        line +='| * '

    for i in range(end+1,word_length):

        line +='| - '

    line +='|'

    return line

def display_guess_matrix(guess_no,word_length,scores) ->None:
    #document
    top_line = '        '
    
    for i in range(1,word_length+1):
        top_line += '| '
        top_line += str(i)
        top_line += ' '
    
    top_line += '| '

    dividing_line = WALL_HORIZONTAL * (9 + 4 * word_length)

    print(top_line)
    print(dividing_line)

    if guess_no == 1:
            print(guess_line)
            print(dividing_line)
    else:
        for i in range(1 , guess_no):
            guess_line = create_guess_line(i+1,word_length)
            guess_line += '   '
        
            guess_line += str(scores[i])
            guess_line += ' Points'
            print(guess_line)
            print(dividing_line)


    

def compute_value_for_guess(word,start_index,end_index,guess)-> int:
    #document
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


        if  select == 'h':
            print(HELP)

        elif select =='q':
            os._exit(0) 

        elif select == 's':
            word=select_word_at_random()
            break

        else:
            print(INVALID)
            
    print('Now try and guess the word, step by step!!')
    print(word) #for test

    word_length=len(word)
    scores = ()

    for guess_no in range(1,len(word)+1):
        
        display_guess_matrix (guess_no,word_length,scores)
        
        Now_enter_Guess = 'Now enter Guess '
        Now_enter_Guess += str(guess_no)
        Now_enter_Guess += ': '
        
        right_guess_len = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1] - GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0] + 1

        while True:
            guess = input(Now_enter_Guess)
            
            if len(guess) == right_guess_len:
                break
        
        start_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]
        end_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]
        Score_for_round = compute_value_for_guess(word,start_index,end_index,guess)
        Score_for_round_tutle = (Score_for_round,)
        scores += Score_for_round_tutle

        if guess_no == len(word):
            whole_guess = guess

    if whole_guess == word :
        print ('You have guessed the word correctly. Congratulations.')

    elif whole_guess != word :
        print ('Your guess was wrong. The correct word was "%s"' % (word))
        

    

if __name__ == "__main__":
	main()