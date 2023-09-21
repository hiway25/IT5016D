# BarEntry.py
# Author: Helen Thomas
# Date: 08.08.2023

year_of_birth = int(input("Please enter the year you were born \n"))
name = input("Please enter your name as appears on your ID \n")
age = 2023 - year_of_birth
not_allowed_names = ['Suzanne May', 'Wiremu Rangi']
allowed_to_enter = age >= 18 and name not in not_allowed_names

if allowed_to_enter:
    print(name, "may enter the bar.")
else:
    print(name, "is not allowed to enter the bar")


