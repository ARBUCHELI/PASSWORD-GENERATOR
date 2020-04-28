# Use an import statement at the top
import random 

word_file = "words.txt" #assign the text file to the word_file variable
word_list = [] #create an empty list

#fill up the word_list
with open('C:/Users/radio/Desktop/ANDRÉS R. BUCHELI - SOFTWARE ENGINEER/COMPUTER SCIENCE/INTRODUCTION TO PYTHON PROGRAMMING/words.txt','r') as words: #opening the file
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)



# test your function
print(generate_password())