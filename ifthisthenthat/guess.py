# this program lets user guess a number between 1 and 9
secret = 7 # fixed secret number
while True: # start loop
    guess = input("Guess the number (1-9): ") # ask user
    guess = int(guess) # convert to int
    if guess == secret: # check answer
        print("Well guessed!") # success message
        break # exit loop
    else: # run this if the guess is wrong
        print("Wrong, try again") # prompt again
