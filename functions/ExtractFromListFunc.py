# ExtractFromListFunc.py
#  Author: Helen Thomas
# Date: 16.08.2023

def extract_first_last(input_list):
    if len(input_list) >= 2:
        return [input_list[0], input_list[-1]]
    else:
        return []

# Example list
list_1 = [5, 10, 15, 20, 25]

# Call the function to extract first and last elements
result_list = extract_first_last(list_1)

print("Original list:", list_1)
print("New list with first and last elements:", result_list)
