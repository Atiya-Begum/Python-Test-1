# Topic:user input
# Question:Ask the user to type a number, then print whether it is even or odd. Remember to convert the input to an integer first.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")