#  ListIterate.py
# Author: Helen Thomas
# Date: 12.08.2023

sample_list = [1, -4, 5, 2, 9, 12, 13]

for item in sample_list:
    print("An item in the sample list is ", item)

#If you need both the index and the item, use the enumerate function:
for index, item in enumerate(sample_list):
    print("The element index is ", index," and the value is ", item)

# If you need oly the index, use range and len:
for index in range(len(sample_list)):
    print("The element index is ", index)

# The list object supports the iterator protocol.  To explicitly
# create an iterator, use the built-in iter function:

i = iter(sample_list)
item = i.__next__()  # fetch first value
print("An item in the sample list is ", item)
item = i.__next__()  # fetch the second value
print("An item in the sample list is ", item)

# Python provides various shortcuts for common list operations.
# For example, if a list contains numbers, the built-in sum function

list_sum = sum(sample_list)
print("\nThe sum of the items in the list is....", list_sum)

subtotal = 30
total = sum(sample_list, subtotal)
print("\nThe sum of the lines in the list and another number is ....", total)

average = float(sum(sample_list)) / len(sample_list)
print("The average of the items in the list is...", average)

# If the list contains strings, you can combine the string into a
# single long string using the join method

haka_list = ["Taringa","whakarongo!","Kia", "rite!","Kia","rite!"]
joined_list = " ".join(haka_list)
print("\nThe joined list is ...", joined_list)


# Accessing elements using negative indices
print("Last element:", sample_list[-1])
print("Second-to-last element:", sample_list[-2])

'''
Assertion test 1; change subtotal value to 30; total will now = 63
Assertion test 2: added a 13 to the list, changes, sum = 46, average = 6.57
Assertion test 3: changed list number to -4; chnages sume = 38, average = 5.4
'''
