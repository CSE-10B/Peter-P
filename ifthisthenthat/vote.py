# this program checks voting eligibility based on age
age = input("Enter your age: ") # get age from user
age = int(age) # convert to integer
if age >= 18: # check if age at least 18
    print("You are eligible to vote") # eligible
else: # run this if age is less than 18
    print("You are not eligible to vote") # not eligible
