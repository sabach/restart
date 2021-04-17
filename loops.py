#loops.py

#Ask the user for a guess.
#Is the guess the right number?
#If the right guess, tell the user it was the right 
#guess and exit the loop.
#If the wrong guess, tell the user it was the wrong
#guess and continue the loop.

import random

random_number=random.randint(1,4100)
isGuessRight = False
print("Welcome to Guess The Number!")
print("The rules are simple. I will think of a number and you try to guess it.")
user_guess=0
while isGuessRight != True:
	for user_guess in range(1,4100):
		#print(user_guess)
		#i=int(user_guess)
		#user_guess=input("guess a number: ")

		if int(user_guess) == random_number:
			print("got the number-{}".format(user_guess))
			isGuessRight=True
			print(user_guess)
		else:
			print("no")
print("got the number-{}".format(random_number))