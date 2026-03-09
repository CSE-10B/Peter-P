# this program converts Celsius to Fahrenheit and Fahrenheit to Celsius
celsius = input("Enter a temperature in Celsius: ") # this asks the user for a Celsius value
celsius = float(celsius) # this changes the Celsius value to a float
fahrenheit = (celsius * 9 / 5) + 32 # this changes Celsius to Fahrenheit
print(celsius, "degrees Celsius is", fahrenheit, "degrees Fahrenheit") # this prints the Celsius to Fahrenheit result

fahrenheit_input = input("Enter a temperature in Fahrenheit: ") # this asks the user for a Fahrenheit value
fahrenheit_input = float(fahrenheit_input) # this changes the Fahrenheit value to a float
celsius_result = (fahrenheit_input - 32) * 5 / 9 # this changes Fahrenheit to Celsius
print(fahrenheit_input, "degrees Fahrenheit is", celsius_result, "degrees Celsius") # this prints the Fahrenheit to Celsius result
