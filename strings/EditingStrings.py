# EditingStrings.py
# Author: Helen Thomas
# DAte: 17.08.2023

string_1 = "Hello World"

# replacing part of a string
print("Replacing part of a string...\n{0}"
      .format(string_1.replace("Hello", "Goodbye")), "\n")

# Changing Upper and Lower case strings
string_2 = "hElLo wOrlD"
print("Making a string upper case...\n{0}"
      .format(string_2.upper()), "\n")

print("Making a string lower case...\n{0}"
      .format(string_2.lower()), "\n")

print("Making a string title case...\n{0}"
      .format(string_2.title()), "\n")

print("Making a string capitalise...\n{0}"
      .format(string_2.capitalize()), "\n")

print("Making a string swap case...\n{0}"
      .format(string_2.swapcase()), "\n")

print("Reversing and inserting characters to a string...\n{0}"
      .format("*".join(reversed(string_2))), "\n")
