# this program prints messages based on value of n
n = input("Enter an integer: ") # take input
n = int(n) # convert to integer
if n % 2 == 1: # check odd
    print("Weird") # odd case
elif n % 2 == 0 and n >= 2 and n <= 5: # even 2-5
    print("Not Weird") # print not weird for 2 to 5
elif n % 2 == 0 and n >= 6 and n <= 10: # even 6-10
    print("Weird") # print weird for 6 to 10
elif n % 2 == 0 and n > 20: # even and greater than 20
    print("Not Weird") # print not weird for numbers above 20
else: # run this for the remaining even numbers
    print("Weird") # print weird for other cases
