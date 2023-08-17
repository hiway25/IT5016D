# ListChangingChallenges.py
# Author: Helen Thomas
# Date: 12.08.2023

import random
import time

# Challenge 1: Prompt user for 3 integers, append to a list, and display the list
def challenge1():
    user_list = []
    for _ in range(3):
        num = int(input("Enter an integer: "))
        user_list.append(num)
    print("User List:", user_list)

# Challenge 2: Modify a proverb list with user input and display the complete proverb
def challenge2():
    proverb_part_list = ["As a man disappears ", " the ", "land remains."]
    print("Proverb parts:")
    for part in proverb_part_list:
        print(part, end="")
    user_input = input("Enter the missing part of the proverb: ")
    proverb_part_list[1] = user_input
    complete_proverb = "".join(proverb_part_list)
    print(complete_proverb)

# Challenge 3: Create a list with 5 random integers (1-10) and display the list
def challenge3():
    random_list = [random.randint(1, 10) for _ in range(5)]
    print("Random List:", random_list)

# Challenge 4: Simulate removing items from a shopping cart list based on user input
def challenge4():
    cart = ["iPhone 7", "MacBook Air", "Surface Tablet"]
    print("Select an item to remove:")
    print("0. iPhone 7\n1. MacBook Air\n2. Surface Tablet")
    choice = int(input("Enter the item number to remove: "))
    if 0 <= choice < len(cart):
        removed_item = cart.pop(choice)
        print("Removed:", removed_item)
    else:
        print("Invalid choice")
    print("Updated Cart:", cart)

# Challenge 5: Reverse a user input word and display the result
def challenge5():
    user_input = input("Enter a word: ")
    reversed_word = user_input[::-1]
    print("Reversed word:", reversed_word)

# Challenge 6: Remove duplicates from a list and display the modified list
def challenge6():
    stored_list = [1, 2, 3, 4, 4, 5, 5, 6, 7, 7]
    unique_list = list(set(stored_list))
    print("List with duplicates removed:", unique_list)

# Challenge 7: Check if a stored list is empty or not
def challenge7():
    stored_list = [1, 2, 3, 4, 5]
    if not stored_list:
        print("The list is empty")
    else:
        print("The list is not empty")

# Challenge 8: Print words longer than a specified length from a stored list
def challenge8():
    stored_list = ["apple", "banana", "grape", "orange", "pear", "strawberry"]
    n = int(input("Enter the minimum word length: "))
    long_words = [word for word in stored_list if len(word) > n]
    print("Words longer than", n, "characters:", long_words)

# Challenge 9: Check if two lists have at least one common member
def challenge9():
    def have_common_member(list1, list2):
        return any(item in list2 for item in list1)
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]
    result = have_common_member(list_1, list_2)
    print("Do the lists have at least one common member?", result)

# Challenge 10: Shuffle and print a stored list
def challenge10():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(my_list)
    print("Shuffled List:", my_list)

# Challenge 11: Demonstrate list append, print, extend behavior
def challenge11():
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    list_1.append(list_2)
    print(list_1)
    list_1.extend(list_2)
    print(list_1)

# Challenge 12: Add random single-digit numbers to a list for 6 seconds and display the final list
def challenge12():
    final_list = []
    for _ in range(6):
        final_list.append(random.randint(0, 9))
        time.sleep(1)
    print("Final List:", final_list)

# Challenge 13: Simulate a lottery drawing 6 numbers from a pool of 1 to 49 without replacement
def challenge13():
    balls = list(range(1, 50))
    picked_balls = []
    for _ in range(6):
        ball = random.choice(balls)
        balls.remove(ball)
        picked_balls.append(ball)
    print("Picked Balls:", picked_balls)

if __name__ == "__main__":
    challenge1()
    challenge2()
    challenge3()
    challenge4()
    challenge5()
    challenge6()
    challenge7()
    challenge8()
    challenge9()
    challenge10()
    challenge11()
    challenge12()
    challenge13()
