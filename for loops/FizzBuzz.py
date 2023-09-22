#  FizzBuzz.py
#  Author: Helen Thomas
#  Date: 11.08.2023

# Replace mulitples as defined by words instead of the number

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
