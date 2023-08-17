# FunctionParameters.py
#  Author: Helen Thomas
# Date: 14.08.2023


# a function that sums all numbers in a stored list
def sum_numbers(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
result = sum_numbers(my_numbers)
print("The sum of the numbers in the list is:", result)

# A function that calculates and displays the number of
# uppercase and lowercase letters ina given string

def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)

# Example usage:
my_string = "Hello.  My name is Helen Thomas"
count_upper_lower(my_string)


# Prompts user for name and phone and trhen outputs formatted text

def display_info(name, phone_number):
    print("Hello there, my name is", name, "and my number is", phone_number + ".")

# Prompt the user for their name and phone number
user_name = input("Please enter your name: ")
user_phone_number = input("Please enter your phone number: ")

# Call the display_info function with the user's input
display_info(user_name, user_phone_number)
