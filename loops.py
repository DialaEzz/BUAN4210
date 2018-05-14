# Write the Python code of the guest game pseudocode
import random
print("\tWelcome to My house Game!") 
print("\nI’m thinking of a number from 1 to 100.")
print("\nTry to guess it in as few attempts as possible.\n")
# set the initial values
my_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1
#Guessing Loop
while guess != my_number :
	if guess > my_number:
		print("Lower…")
	else:
		print("Higher…")
	guess = int(input("take a guess: "))
	tries += 1
Print("You guessed it! The number was " , my_number)
Print("and it only took you ", tries, "tries!\n")

input("\n\nPress Enter to exit.")
