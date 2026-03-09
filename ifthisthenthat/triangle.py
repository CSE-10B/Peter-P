# this program checks if a triangle is equilateral
side1 = input("Enter side 1: ") # get first side
side2 = input("Enter side 2: ") # get second side
side3 = input("Enter side 3: ") # get third side
side1 = float(side1) # convert to float
side2 = float(side2) # convert to float
side3 = float(side3) # convert to float
if side1 == side2 and side2 == side3: # all sides equal
    print("It is an equilateral triangle") # print result
else: # run this if all sides are not equal
    print("It is not an equilateral triangle") # print result
