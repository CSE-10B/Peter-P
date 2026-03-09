# this program converts between Celsius and Fahrenheit
# get celsius from user
c = input("Enter temperature in Celsius: ") # ask for celsius value
c = float(c) # convert to float
# calculate fahrenheit
f_from_c = (c * 9/5) + 32 # formula to convert
print(c, "°C is", f_from_c, "in Fahrenheit") # display result

# get fahrenheit from user
f = input("Enter temperature in Fahrenheit: ") # ask for fahrenheit value
f = float(f) # convert to float
# calculate celsius
c_from_f = (f - 32) * 5/9 # formula to convert
print(f, "°F is", c_from_f, "in Celsius") # display result
