
GUESS_INDEX_TUPLE = (
	((0,1),(2,4),(2,4),(3,5),(2,5),(0,5)),						# word length 6
	((0,1),(1,2),(4,6),(2,5),(3,6),(2,6),(0,6)),				# word length 7
	((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(2,7),(0,7)),			# word length 8
	((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(3,7),(2,8),(0,8))		# word length 9
)

#print (GUESS_INDEX_TUPLE[1][1],end='\n')
#print (GUESS_INDEX_TUPLE[2][1])
#print (len(GUESS_INDEX_TUPLE))

def create_guess_line(guess_no,word_length)->str:
	(start,end)=GUESS_INDEX_TUPLE[word_length-6][guess_no-1]
	
	line='Guess '
	guess_no_str=str(guess_no)
	line+=guess_no_str
	line+=' '
	
	for i in range(0, start):
		
		line += '| - '
	
	for i in range(start,end+1):
		
		line +='| * '
	
	for i in range(end+1,word_length):
		
		line +='| - '
	
	line +='|'

	#print (line)	#for test
	return line


create_guess_line(1,9)