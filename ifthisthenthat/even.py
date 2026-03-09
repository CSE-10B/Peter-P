# this program checks if a number is even or odd
num = input("Enter a number: ") # take input from user
num = int(num) # convert input to integer
if num % 2 == 0: # check remainder when divided by 2
    print(num, "is even") # print even message
else: # run this if the number is not even
    print(num, "is odd") # print odd message
