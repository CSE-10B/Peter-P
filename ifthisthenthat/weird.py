# this program prints Weird or Not Weird based on the rules
n = input("Enter an integer: ") # this asks the user for an integer
n = int(n) # this changes the input to an integer
if n % 2 == 1: # this checks if the number is odd
    print("Weird") # this prints Weird for odd numbers
elif n >= 2 and n <= 5: # this checks if the number is from 2 to 5
    print("Not Weird") # this prints Not Weird for numbers from 2 to 5
elif n >= 6 and n <= 10: # this checks if the number is from 6 to 10
    print("Weird") # this prints Weird for numbers from 6 to 10
elif n > 20: # this checks if the number is greater than 20
    print("Not Weird") # this prints Not Weird for numbers greater than 20
else: # this runs for the remaining numbers
    print("Weird") # this prints Weird for the remaining numbers
