# SleepCalculator.py
# Author: Helen Thomas
# Date: 01.08.23

print("Welcome to your Sleep Calculator\n")
user_yob = int(input("Please enter your year of birth...\n"))
hours_slept = int((2023 - user_yob) * 365 * 7)

print("Thank you for your input\n")
print("The number of hours you have slept in your life is ", hours_slept)
