#  ContinueStatement.py
#  Author: Helen Thomas
# Date: 11.08.2023

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=" ")
