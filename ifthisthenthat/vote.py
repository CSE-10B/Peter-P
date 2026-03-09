# this program checks if a person can vote
age = input("Enter your age: ") # this asks the user for an age
age = int(age) # this changes the input to an integer
if age >= 18: # this checks if the age is 18 or more
    print("You are eligible to vote") # this prints that the person can vote
else: # this runs if the age is less than 18
    print("You are not eligible to vote") # this prints that the person cannot vote
