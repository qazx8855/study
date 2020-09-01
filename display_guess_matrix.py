WALL_VERTICAL = "|"
WALL_HORIZONTAL = "-"
from create_guess_line import *

def display_guess_matrix(guess_no,word_length,scores) ->None:
    
    top_line = '        '
    
    for i in range(1,word_length+1):
        top_line += '| '
        top_line += str(i)
        top_line += ' '
    
    top_line += '| '

    dividing_line = WALL_HORIZONTAL * (10 + 4 * word_length)

    print(top_line)
    print(dividing_line)

    for i in range(0 , guess_no):
        guess_line = create_guess_line(i+1,word_length)
        guess_line += '   '
        if i = 0:
            print(guess_line)
            print(dividing_line)
        
        elif i > 0 :
            guess_line += str(scores[i])
            guess_line += ' Points'
            print(guess_line)
            print(dividing_line)
        
        

        
        
        
    

scores = (26,10,67,18) #test
display_guess_matrix(1,6,scores)