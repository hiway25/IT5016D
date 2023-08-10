#  SquareBrackets.py
#  Author: Helen Thomas
# Date:  10.08.2023

# Write a program with a while loop that prints 1 through to n in square brackets. For example, if the user enters 6 then the program should display
# [1] [2] [3] [4] [5] [6]

n = int(input("Enter a number:  "))
count = 1

print("[", end="")

while count <= n:
    if count == n:
        print("[" + str(count) + "]")
    else:
        print("[" + str(count) + "]", end="  ")
    count += 1

