# this program prints day name based on number input
num = input("Enter a number (1-7): ") # get input from user
num = int(num) # convert to integer
if num == 1: # check each number
    print("Monday") # print day
elif num == 2: # check if number is 2
    print("Tuesday") # print day
elif num == 3: # check if number is 3
    print("Wednesday") # print day
elif num == 4: # check if number is 4
    print("Thursday") # print day
elif num == 5: # check if number is 5
    print("Friday") # print day
elif num == 6: # check if number is 6
    print("Saturday") # print day
elif num == 7: # check if number is 7
    print("Sunday") # print day
else: # run this if the number is outside 1 to 7
    print("Invalid number") # handle wrong input
