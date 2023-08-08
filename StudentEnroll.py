# StudentEnroll.py
# Author: Helen Thomas
# Date: 08.08.2023

lives_less_than_4km = True
is_less_than_18 = False
right_to_nz = True

# Test case assertion 1: result should be True
print("The student can enroll in our school without international fees...\n")
print(lives_less_than_4km
      and right_to_nz
      and not is_less_than_18,"\n")

# Test case assertion 2: result should be False
print("The student can enroll in our school without international fees...\n")
print(lives_less_than_4km
      and right_to_nz
      and is_less_than_18,"\n")

# Test case assertion 3: result should be False
print("This student can enroll in our school..\n")
print(right_to_nz
      and is_less_than_18
      and not lives_less_than_4km,"\n")


# answers given in course

distance_from_school = 3
age_in_years = 14
has_residency = True
is_fee_foreign = False
print("This program works out eligibility for enrolment....\n")

# Test case assertion 1: result should be True
print("The student's eligibility to enrol is ",
      distance_from_school < 4
      and age_in_years < 18
      and has_residency
      or age_in_years < 18
      and is_fee_foreign, "\n")

print("The student waited for too long...\n")
age_in_years = 18

# Test case assertion 2: result should be False
print("The student's eligibility to enrol now is ",
      distance_from_school < 4
      and age_in_years < 18
      and has_residency
      or age_in_years < 18
      and is_fee_foreign, "\n")