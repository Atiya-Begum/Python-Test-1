#Topic:user input
#Question:  Ask the user for a city name and a temperature (as a float), then print a sentence combining both, like: It is 30.5 degrees in Mumbai.

city = input("enter the city name ")
temperature = float(input("enter temperature"))

print(f"It is {temperature} degrees in {city}.")