# MoreTuples.py
# Author: Helen Thomas
# Date ; 12.08.2023

# Challenge 1: Create a tuple
tuple1 = (1, 2, 3, 4, 5)

# Challenge 2: Create a tuple with different data types
tuple2 = (1, "apple", 3.14, True, "banana")

# Challenge 3: Create a tuple with 5 numbers and print the 3rd number
tuple3 = (10, 20, 30, 40, 50)
print("The 3rd number in tuple3:", tuple3[2])

# Challenge 4: Create a tuple with 3 strings and extract each element into separate variables
tuple4 = ("cat", "dog", "elephant")
animal1, animal2, animal3 = tuple4

# Challenge 5: Create a 6 element integer tuple and print the 4th and 4th from last elements
tuple5 = (1, 2, 3, 4, 5, 6)
print("4th element:", tuple5[3])
print("4th from last element:", tuple5[-4])

# Challenge 6: Print repeated items of a tuple (only once regardless of duplicates)
tuple6 = (1, 2, 3, 2, 4, 5, 4)
unique_items = set(tuple6)
print("Unique items in the tuple:", unique_items)

# Challenge 7: Check if a value is contained in a tuple, including duplicates
tuple7 = (1, 2, 3, 2, 4, 5, 4)
value_to_check = int(input("Enter a value to check: "))
count_of_value = tuple7.count(value_to_check)
if count_of_value > 0:
    print("The tuple contains", value_to_check)
    if count_of_value > 1:
        print("And it appears", count_of_value, "times")
else:
    print("The tuple does not contain", value_to_check)
