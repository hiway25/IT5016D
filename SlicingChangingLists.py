# SlicingChangingLists.py
# Author: Helen Thomas
# Date: 12.08.2023

list_1 = [ 34, 123, 5, 77, 59, 2, 4 ]
list_2 = [23, 15, 63, 255, 88, 64, 844, 1]

print(list_1[2:5])

def get_first_half(lst):
    if len(lst) % 2 == 0:
        return lst[:len(lst) // 2]
    else:
        return "The list does not have an even number of elements"

# Example list with an even number of elements (at least 6 elements)


# Call the function to get the first half of the elements
result = get_first_half(list_2)

# Display the result
print("First half of the elements:", result)

# Write a program that returns the last quarter of all the elements
# of any list whose total number of elements is a multiple of four.

def get_last_quarter(lst):
    if len(lst) % 4 == 0:
        return lst[3 * len(lst) // 4:]
    else:
        return "The list does not have a total number of elements that is a multiple of four"


# Call the function to get the last quarter of the elements
result = get_last_quarter(list_2)

# Display the result
print("Last quarter of the elements:", result)
