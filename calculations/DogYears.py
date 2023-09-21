# DogYears.py
# Author: Helen Thomas
# Date: 11.08.2023

def dog_age(human_age):
    if human_age <= 2:
        dog_years = human_age * 10.5
    else:
        dog_years = 21 + (human_age - 2) * 4
    return dog_years

# Get input from the user
human_years = int(input("Enter the dog's age in human years: "))

# Call the dog_age function and print the result
dog_years = dog_age(human_years)
print("The dog's age in dog years is:", dog_years)
