# this program prints the day for a number from 1 to 7
num = input("Enter a number from 1 to 7: ") # this asks the user for a number
num = int(num) # this changes the input to an integer
if num == 1: # this checks if the number is 1
    print("Monday") # this prints Monday
elif num == 2: # this checks if the number is 2
    print("Tuesday") # this prints Tuesday
elif num == 3: # this checks if the number is 3
    print("Wednesday") # this prints Wednesday
elif num == 4: # this checks if the number is 4
    print("Thursday") # this prints Thursday
elif num == 5: # this checks if the number is 5
    print("Friday") # this prints Friday
elif num == 6: # this checks if the number is 6
    print("Saturday") # this prints Saturday
elif num == 7: # this checks if the number is 7
    print("Sunday") # this prints Sunday
else: # this runs if the number is not from 1 to 7
    print("Invalid number") # this prints an invalid number message
