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
    '''
    This function will first judge the input parameters is 'FIXED' or 'ARBITRARY' or not,
    if the answer is yes, then it will load word list form corresponding text file, and 
    then it will create a random number from range of length of word list. Finally, it will
    return a random word. If the input is not 'FIXED' or 'ARBITRARY', the function will 
    return None.
    '''

    if  word_select == 'FIXED' or word_select =='ARBITRARY'  :
        word_list = load_words(word_select)
        number = random_index(word_list)
        word = word_list[number]
        return word
    else:
        return None      


def create_guess_line(guess_no,word_length)->str:
    '''
    This function is used to create a guess line, which include two parts: 
    1.Guess number (To show how many times the user guess)
    2.Create a one line matrix by using loop to show the position of the guessed alphabet.
    These will be saved in a string and the string will be returned in the end. 
    '''
    
    (start,end)=GUESS_INDEX_TUPLE[word_length-6][guess_no-1]

    #Create Guess number
    line='Guess '          
    line+=str(guess_no)
    
    #Create guess line matrix
    for i in range(0, start):       
        line += '| - '

    for i in range(start,end+1):
        line +='| * '

    for i in range(end+1,word_length):
        
        line +='| - '

    line +='|'
    return line


def display_guess_matrix(guess_no,word_length,scores) ->None:
    '''
    This function is focus on create a guess matrix which include three parts:
    1. The top line which used as title
    2. A dividing line by use several '-'
    3. Use function 'create_guess_line' repeatedly .
    '''

    #Create top line
    top_line = '       '
    
    for i in range(1,word_length+1):
        top_line += '| '
        top_line += str(i)
        top_line += ' '
    
    top_line += '|'

    #Create dividing_line
    dividing_line = WALL_HORIZONTAL * (9 + 4 * word_length)

    #Print title
    print(top_line)
    print(dividing_line)

    #Create and print martix
    #Create and print martix in user first guess
    if guess_no == 1:
        guess_line = create_guess_line(guess_no,word_length)
        print(guess_line)
        print(dividing_line)

    #Create and print martix in user guess(Not first guess)
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
    '''
    This function will count how many scores the user will get in one guess.
    '''

    scores = 0
    #Cut whole word to get right answer. 
    right_guess = word[start_index:end_index+1]  
    
    for i in range(0,len(right_guess)):
        
        #
        if guess[i] == right_guess[i]:
            if guess[i] in VOWELS:
                scores += 14
            
            elif guess[i] in CONSONANTS:
                scores += 12
        
        elif guess[i] in right_guess and guess[i] != right_guess[i] :
                scores += 5
    
    return scores
    

def main()->None:
    '''
    Handles top-level interaction with user.
    '''
    # Write the code for your main function here

    print (WELCOME)

    while True:
        select=input(INPUT_ACTION)

        if select not in ('s','h','q'):
            print(INVALID)
            
        elif select == 'h':
            print(HELP)
            break
        elif select =='q':
            return None

        elif select == 's':
            break

    while True:
        word_select = input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
        word = select_word_at_random(word_select)

        if word != None: 
            break
    
    print('Now try and guess the word, step by step!!')
                
    word_length = len(word)
    scores = ()

    for guess_no in range(1,len(word)):
        
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

    guess_no = word_length
    display_guess_matrix (guess_no,word_length,scores)
            
    guess = input('Now enter your final guess. i.e. guess the whole word: ')

    if guess == word :
        print ('You have guessed the word correctly. Congratulations.')

    elif guess != word :
        print ('Your guess was wrong. The correct word was "%s"' % (word))
    
                
if __name__ == "__main__":
	main()