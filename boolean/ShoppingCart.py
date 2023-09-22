# ShoppingCart.py
# Author: Helen Thomas
# 08.08.2023

they_are_registered = True
at_least_1_shopping_cart_item = False

# Test case assertion: result should be True
print("This user can make a purchase....\n")
print(they_are_registered
      and not at_least_1_shopping_cart_item, "\n")

# Test assertion: result should be True
print("This user can make purchase on a guest account....\n")
print(at_least_1_shopping_cart_item
      and not they_are_registered, "\n")

# Test assertion: result should be True
print("This user can purchase gift cards....\n")
print(not they_are_registered
      and not at_least_1_shopping_cart_item, "\n")
