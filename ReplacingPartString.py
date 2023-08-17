#  ReplacingPartString.py
# Author: Helen Thomas
# Date: 17.08.2023

# t takes a user input sentence and replaces all the spaces with dashes before displaying the output

user_input = input("Please enter a sentence: ")

# Replace spaces with dashes
output = user_input.replace(" ", "-")

print("Output with spaces replaced:", output)


#  randomly selects a character from a stored string and then inserts that
#  character between every character in the string:
import random

def insert_random_char(input_string, char):
    return char.join(input_string)

stored_string = "Hello"
random_char = random.choice(stored_string)

result_string = insert_random_char(stored_string, random_char)

print("Original string:", stored_string)
print("Random character:", random_char)
print("Result string with random character inserted:", result_string)


#Capitalise every 5th letter in a string
def capitalize_every_fifth(input_string):
    result = ""
    for i, char in enumerate(input_string):
        if(i + 1) % 5 == 0:
            result += char.upper()
        else:
            result += char
    return result

test_case = "The only thing that scares me is Keyser Soze."
result = capitalize_every_fifth(test_case)
result_with_asterisks = "*".join(result.split())

print("Original string:", test_case)
print("Transformed string:", result_with_asterisks)

