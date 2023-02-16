
print("Enter a word or sentence, and I will tell you a story")
word = (str(input())).lower()


while True: 
	if word.isdigit():
		print('Buzz sound! Try enter a word next time.')
		word = str(input())
	elif word == "": 
		print('You kinda forgot to enter a word, there.')
		word = str(input())
	else:
		break


v = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
c = len(word) - v
l = len(word)

print('Your story consists of %s letters, %s vowels, and %s consonants. Exciting, right?' % (l, v, c))



