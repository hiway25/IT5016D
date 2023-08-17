# FunctionExercises.py
# Author: Helen Thomas
# DAte: 15.08.2023

#Challenge 2
def sum(num1, num2):
    return num1 + num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = sum(num1, num2)
print("The sum of ", num1, "and", num2, "is", result)

def fill_list(input_list):
    while len(input_list) < 3:
        item = input("Enter an item to fill the list: ")
        input_list.append(item)

list_a = ["brown", "grey", "amber"]
list_b = ["red", "green"]
list_c = ["purple"]

list_d = [list_a, list_b, list_c]

print("Original lists:")
print("List A:", list_a)
print("List B:", list_b)
print("List C:", list_c)

for sublist in list_d:
    fill_list(sublist)

print("\nUpdated lists:")
print("List A:", list_a)
print("List B:", list_b)
print("List C:", list_c)



# Online store activity
def calculate_item_total(item_name, price, quantity):
    return price * quantity

print("Welcome to the Online Store!")

items = [
    {"name": "Greenstone Koru carving", "price": 265},
    {"name": "Rimu Tiki necklace", "price": 42},
    {"name": "Manaia bone earrings", "price": 311}
]

total_amount = 0

for item in items:
    quantity = int(input("Enter the quantity of '{}' you want to purchase: ".format(item["name"])))
    item_total = calculate_item_total(item["name"], item["price"], quantity)
    total_amount += item_total
    print("Total for '{}' is ${}".format(item["name"], item_total))

# Calculate the GST (15%)
gst_amount = total_amount * 0.15
total_amount_with_gst = total_amount + gst_amount

print("Overall total (including 15% GST): ${:.2f}".format(total_amount_with_gst))
