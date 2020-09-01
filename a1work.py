"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

# Fill these in with your details
__author__ = "{{user.name}} ({{user.id}})"
__email__ = ""
__date__ = ""

#import here    
import sys
import random
GUESS_INDEX_TUPLE = (
	((0,1),(2,4),(2,4),(3,5),(2,5),(0,5)),						# word length 6
	((0,1),(1,2),(4,6),(2,5),(3,6),(2,6),(0,6)),				# word length 7
	((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(2,7),(0,7)),			# word length 8
	((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(3,7),(2,8),(0,8))		# word length 9
)
WALL_VERTICAL = "|"
WALL_HORIZONTAL = "-"

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


# Write your code here (i.e. functions)


def main():
	"""
	Handles top-level interaction with user.
	"""
	# Write the code for your main function here
    
    WELCOME = """
    Welcome to the Criss-Cross Multi-Step Word Guessing Game!
    """

    INPUT_ACTION = """
    Enter an input action. Choices are:
    s - start game
    h - get help on game rules
    q - quit game: 
    """

    HELP = """
    Game rules - You have to guess letters in place of the asterixis. 
    Each vowel guessed in the correct position gets 14 points. 
    Each consonant guessed in the correct position gets 12 points. 
    Each letter guessed correctly but in the wrong position gets 5 points. 
    If the true letters were "dog", say, and you guessed "hod", 
    you would score 14 points for guessing the vowel, "o", in the correct 
    position and 5 points for guessing "d" correctly, but in the 
    incorrect position. Your score would therefore be 19 points.
    """

    INVALID = """
    Please enter a valid command.
    """
    print(WELCOME)
    select=input(INPUT_ACTION)

    if  select == 'h':
        print(HELP)
    elif select =='q':
        sys.exit(0)
    elif select == 's':
        difficult()

def load_words(word_select):
	"""
	Loading in the selection of words from either the FIXED or ARBITRARY word
	length.

	Parameters:
		word_select (str): "FIXED" or "ARBITRARY" word sets.
	Returns:
		(tuple<str>): A tuple containing all the words.
	"""
	words = ()
	
	with open(f"WORDS_{word_select}.txt", "r") as file:
		file_contents = file.readlines()
	
	for line in file_contents:
		word = line.strip()
		if word != '':
			words += (word,)

	return words



def difficult():
    difficult=input("Do you want a "FIXED" or "ARBITRARY" length word?")
    if difficult =='FIXED':
        load_words('FIXED')
    elif difficult =='ARBITRARY'    
        load_words(ARBITRARY)








def random_index(words):
	"""
	(int): Returns an int representing the index for the word to be guessed.
	"""
	return random.randrange(0, len(words))





if __name__ == "__main__":
	main()