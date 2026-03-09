# this program checks if a number is even or odd
num = input("Enter a number: ") # this asks the user for a number
num = int(num) # this changes the input to an integer
if num % 2 == 0: # this checks if the number is divisible by 2
    print(num, "is even") # this prints that the number is even
else: # this runs if the number is not divisible by 2
    print(num, "is odd") # this prints that the number is odd
