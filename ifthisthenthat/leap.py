# this program checks if a year is a leap year
year = input("Enter a year: ") # input year
year = int(year) # convert to integer
# apply leap year rules
if year % 400 == 0: # divisible by 400
    print(True) # leap year
elif year % 100 == 0: # divisible by 100 but not 400
    print(False) # not leap year
elif year % 4 == 0: # divisible by 4 but not 100
    print(True) # leap year
else: # run this if none of the leap year rules match
    print(False) # not leap year
