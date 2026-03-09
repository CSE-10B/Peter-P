# this program lets the user guess a random number from 1 to 9
import random # this lets the program choose a random number

secret_number = random.randint(1, 9) # this picks a random number from 1 to 9
guess = input("Guess the number from 1 to 9: ") # this asks the user for a guess
guess = int(guess) # this changes the guess to an integer
while guess != secret_number: # this keeps looping while the guess is wrong
    print("Wrong, try again") # this tells the user the guess is wrong
    guess = input("Guess the number from 1 to 9: ") # this asks for another guess
    guess = int(guess) # this changes the new guess to an integer
print("Well guessed!") # this prints the success message
