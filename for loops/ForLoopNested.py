#  ForLoopNested.py
#  Author: Helen Thomas
#  Date: 11.08.2023

 # Write a program that will ask the user for a message and the number of times they want that message displayed

user_input = int(input("Please enter a number for the size "
                       "of the shape you wish to create"))

for i in range(user_input):
    for j in range(i):
        print('* ', end="")
    print("")

for i in range(user_input, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')


