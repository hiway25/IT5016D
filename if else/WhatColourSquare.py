# WhatColourSquare.py
# Author: Helen Thomas
# Date: 09.08.2023

# Read position coordinates from user

column = input("Enter the column letter: ").lower()
row = int(input("Enter the row number:  "))

#  Determine if the column starts with a black or white square
if column in "aceg":
    column_starts_with_black = True
else:
    column_starts_with_black = False

#  Use modular arithmetic to determine the color of the square in that row
if(row % 2 == 0 and column_starts_with_black) or (row % 2 != 0 and not column_starts_with_black):
    square_colour = "white"
else:
    square_colour = "black"

print("The square at", column, row, "is", square_colour, ".")

