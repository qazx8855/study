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

WORDS=load_words('FIXED')
print (WORDS)