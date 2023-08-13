#  ListChallenges
#  Author: Helen Thomas
#  12.08.2023

list_1 = [23,66,23,12]
list_2 = [1,19,4,8]
list_3 = ["land of","the","the long white cloud"]



# Output the list with the most elements from list_2 and list3:
if len(list_2) > len(list_3):
    print("List with the most elements:", list_2)
else:
    print("List with the most elements:", list_3)


#  Output every odd valued index item from list_1
for i in range(len(list_1)):
    if i % 2 == 1: #check if index is odd
        print("Items at odd index,", i, ":", list_1[i])

# Output strings from list3 in order from shortest to longest,
# formatted as a single string:

sorted_list_3 = sorted(list_3, key=len) # sort list by string length
formatted_string = "  ".join(sorted_list_3)  # join the sorted list into a string
print("Sorted and formatted string:", formatted_string)

# Randomly select 2 different integers from list2
import random

# ensure the list has at least two unique integers
if len(list_2) >= 2:
    random_indices = random.sample(range(len(list_2)), 2)
    random_integers = [list_2[i] for i in random_indices]
    print("Randomly selected integers:", random_integers)
else:
    print("List does not have enough unique integers")

#The user must be prompted and given a choice to see either the sum or the average
# of the combined lists. Assume that the user enters valid integers only.
'''def get_sum(list_1, list_2):
    return sum(list1 + list2)

def get_average(list_1, list_2):
    combined_list = list_1 + list_2
    return sum(combined_list) / len(combined_list)

# First 2 lists
list_1 = [23, 66, 23, 12]
list_2 = [1, 19, 4, 8]

print("List 1:", list_1)
print("List 2:", list_2)

# Prompt user for choice
print("Choose an option:")
print("1. Sum of combined lists")
print("2. Average of combined lists")

choice = int(input("Enter your choice (1 or 2): "))

# Validate the user's choice
if choice == 1:
    result = get_sum(list_1, list_2)
    print("Sum of the combined lists:", result)
elif choice == 2:
    result = get_average(list_1, list_2)
    print("Average of the combined lists:", result)
else:
    print("Invalid choice. Please enter 1 or 2.")'''

list_1.extend(list_2)
print(list_1)