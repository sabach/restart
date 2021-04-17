# Write a Python program to guess a number between 1 to 9. 
#Note : User is prompted to enter a guess.
#If the user guesses wrong then the prompt appears again
#until the guess is correct, on successful guess,
#user will get a "Well guessed!" message, 
#and the program will exit.

from numpy import random
randonly_selected=random.randint(10)
guessed_number=input("Type your number to Guess: ")

while randonly_selected == int(guessed_number):
	guessed_number=input("Type your number to Guess: ")
	print (randonly_selected, guessed_number)