# WhatTypeTriangle.py
# Author: Helen Thomas
# Date: 09.08.2023

#Scalene triangle: all sides have different lengths
#Isoceles triangle: Two sides have the same length
#Equilateral triangle: all sides are equal.

a = int(input("The length of side a =  \n"))
b = int(input("The length of side b =  \n"))
c = int(input("The length of side c =  \n"))

if a != b and b != c:
    print("This is a scalene triangle.")
elif a == b and b == c:
    print("This is an equilateral triangle.")
else:
    print("This is an isoceles triangle.")
