WALL_VERTICAL = "|"
WALL_HORIZONTAL = "-"
from create_guess_line import *
from a1_support import *
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
        
scores = (26,10,67,18) #test
display_guess_matrix(2,6,scores)
word = load_words('FIXED')
