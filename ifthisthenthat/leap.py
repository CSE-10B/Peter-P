# this program checks if a year is a leap year
year = input("Enter a year: ") # this asks the user for a year
year = int(year) # this changes the input to an integer
if year % 400 == 0: # this checks if the year is divisible by 400
    print(True) # this prints True because the year is a leap year
elif year % 100 == 0: # this checks if the year is divisible by 100
    print(False) # this prints False because the year is not a leap year
elif year % 4 == 0: # this checks if the year is divisible by 4
    print(True) # this prints True because the year is a leap year
else: # this runs if the year is not divisible by 4
    print(False) # this prints False because the year is not a leap year
