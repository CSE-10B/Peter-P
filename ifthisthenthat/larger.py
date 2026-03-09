# this program prints the larger of two numbers
num1 = input("Enter the first number: ") # this asks the user for the first number
num2 = input("Enter the second number: ") # this asks the user for the second number
num1 = float(num1) # this changes the first number to a float
num2 = float(num2) # this changes the second number to a float
if num1 > num2: # this checks if the first number is larger
    print("The first number is larger") # this prints that the first number is larger
elif num2 > num1: # this checks if the second number is larger
    print("The second number is larger") # this prints that the second number is larger
else: # this runs if the numbers are equal
    print("Both numbers are equal") # this prints that both numbers are equal
