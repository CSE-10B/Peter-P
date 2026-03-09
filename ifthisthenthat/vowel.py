# this program checks if a character is a vowel
char = input("Enter a character: ") # this asks the user for a character
char = char.lower() # this changes the character to lowercase
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u": # this checks if the character is a vowel
    print(char, "is a vowel") # this prints that the character is a vowel
else: # this runs if the character is not a vowel
    print(char, "is not a vowel") # this prints that the character is not a vowel
