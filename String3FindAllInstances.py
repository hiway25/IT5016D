#  String3FindAllInstances.py
#  Author: Helen Thomas
#  Date: 17.08.2023

string_1 = "Ka mate kainga tahi ka ora kainga rua."

print("Does this string start with Ka?...{0}\n".format(string_1.startswith("Ka")))

print("Does this string start with Tr?...{0}\n".format(string_1.startswith("Tr")))

print("Does this string end with rua?...{0}\n".format(string_1.endswith("rua.")))

# other functions
"""
string_1.isalnum()         #check if all char are alphanumeric 
string_1.isalpha()         #check if all char in the string are alphabetic
string_1.isdigit()         #test if string contains digits
string_1.istitle()         #test if string contains title words
string_1.isupper()         #test if string contains upper case
string_1.islower()         #test if string contains lower case
string_1.isspace()         #test if string contains spaces
"""