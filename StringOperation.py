#Storing a string values and counting


#Asking the user for an entry
sentence = input("Please enter a sentence: ")

#counting the characters and words
char_count = len(sentence)
word_count = len(sentence.split())

#print the counts for words and characters
print("character count is", char_count)
print("Word Count is", word_count)