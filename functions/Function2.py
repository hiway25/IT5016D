# Function2.py
#  Author: Helen Thomas
#  DAte: 14.08.2023

def show_welcome():
    print("Welcome to our program.")

def add_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b

print (add_numbers(3, 6))

"""Program to Display a String x Times:"""
def display_text_multiple_times(text, times):
    for _ in range(times):
        print(text)

print("Welcome to the Text Display Program!")

# Input the values
x = 6 # You can change this value
y = "Hello, World!"  # You can change this value

# Call the display_text_multiple_times function
display_text_multiple_times(y, x)

""". Program to Output a Random Number or Terminate:"""
import random

def random_number_program():
    print("Welcome to the Random Number Program!")

    while True:
        user_input = input("Type 'r' to get a random number, or anything else to quit: ")

        if user_input.lower() == 'r':
            random_number = random.randint(1, 100)
            print("Random number: {}".format(random_number))
        else:
            print("Goodbye!")
            break

# Call the random_number_program function to start the program
random_number_program()
