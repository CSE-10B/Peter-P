# this program prints the larger of two numbers
num1 = input("Enter first number: ") # first input
num2 = input("Enter second number: ") # second input
num1 = float(num1) # convert to float
num2 = float(num2) # convert to float
if num1 > num2: # compare numbers
    print(num1, "is larger") # print larger
elif num2 > num1: # check if second number is larger
    print(num2, "is larger") # print larger
else: # run this if both numbers are the same
    print("Both numbers are equal") # they are same
