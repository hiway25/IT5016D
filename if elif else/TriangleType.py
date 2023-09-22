#  TriangleType.py
#  Author: Helen Thomas
#  Date: 11.08.2023

def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input: Side lengths must be positive"

    # Check the triangle inequality theorem
    if a >= b + c or b >= a + c or c >= a + b:
        return "Not a valid triangle"

    # Check if it's an equilateral triangle
    if a == b and b == c:
        return "Equilateral triangle"
    # Check if it's a scalene triangle
    elif a != b and a != c and b != c:
        return "Scalene triangle"
    # If it's not equilateral or scalene, it's isosceles
    else:
        return "Isosceles triangle"


# Get input from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Call the triangle_type function and print the result
triangle_result = triangle_type(side1, side2, side3)
print("The triangle is:", triangle_result)
