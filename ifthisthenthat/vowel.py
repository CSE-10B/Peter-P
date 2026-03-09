# this program checks if a character is a vowel or not
char = input("Enter a single character: ") # get input from user
# convert to lowercase to handle uppercase vowels
char = char.lower() # make character lowercase
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u': # check if the character is a vowel
    print(char, "is a vowel") # print vowel message
else: # run this if it is not a vowel
    print(char, "is not a vowel") # print not vowel message
