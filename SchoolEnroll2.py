# SchoolEnroll2.py
# Author: Helen Thomas
# Date: 08.08.2023

age_in_years= int(input("Please enter your age in years  \n"))
distance_from_school = int(input("How far in 'km' is your home from the school?"))

print("The student's eligibility to enrol now is ",
      distance_from_school < 5
      and 10 < age_in_years < 18)

