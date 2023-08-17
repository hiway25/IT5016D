# SplittingStringsEx.py
# Author: Helen Thomas
# DAte: 18.08.2023

# USing the shuffle function
import random

def jumble_words(sentence):
    words = sentence.split()
    random.shuffle(words)
    return " ".join(words)

stored_sentence = "This is a stored sentence that we want to jumble."

jumbled_sentence = jumble_words(stored_sentence)

print("Original sentence:", stored_sentence)
print("Jumbled sentence:", jumbled_sentence)


#  radius calculator
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

print("Welcome to the Circle Area Calculator!")

radius = float(input("Please enter the radius of the circle: "))

circle_area = calculate_circle_area(radius)

print("The area of the circle with radius", radius, "is:", circle_area)


# finding longest word length in a list

def find_longest_word_length(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

word_list = ["apple", "banana", "grape", "kiwi", "watermelon", "strawberry"]

longest_word_length = find_longest_word_length(word_list)

print("List of words:", word_list)
print("Length of the longest word:", longest_word_length)

# Write a program to remove the nth word from a string containing words separated by spaces.
def remove_nth_word(input_string, n):
    words = input_string.split()
    if 1 <= n <= len(words):
        del words[n - 1]
        return " ".join(words)
    else:
        return "Invalid value of n"

input_string = "This is a sample string containing words."
print("Original string:", input_string)
n = int(input("Enter the position of the word to remove: "))

result_string = remove_nth_word(input_string, n)
print("String after removing the nth word:", result_string)

# Write a program that accepts a comma separated sequence of words as input
# and prints the unique words.
def print_unique_words(input_string):
    words = input_string.split(",")
    unique_words = set(words)
    for word in unique_words:
        print(word.strip())  # Removing leading/trailing spaces

input_sequence = input("Enter a comma-separated sequence of words: ")

print("Unique words:")
print_unique_words(input_sequence)



