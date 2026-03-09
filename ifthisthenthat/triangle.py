# this program checks if a triangle is equilateral
side1 = input("Enter side 1: ") # this asks the user for side 1
side2 = input("Enter side 2: ") # this asks the user for side 2
side3 = input("Enter side 3: ") # this asks the user for side 3
side1 = float(side1) # this changes side 1 to a number
side2 = float(side2) # this changes side 2 to a number
side3 = float(side3) # this changes side 3 to a number
if side1 == side2 and side2 == side3: # this checks if all sides are equal
    print("It is an equilateral triangle") # this prints that it is equilateral
else: # this runs if all sides are not equal
    print("It is not an equilateral triangle") # this prints that it is not equilateral
