# RemoveContentString.py
# Author: Helen Thomas
# Date: 17.08.2023

string_1 = "Hello World"
# Strip off newline characters from end of string_1
string_1.strip("\n")

# strip() removes from both ends
# lstrip() removes leading characters (Left-strip)
# rstrip() removes trailing characters

string_2 = "  xyz  "
# showing string strip
print("Original string is ...\n")
print("***",string_2,"***\n")
print("Using strip()...\n")
print("***",string_2.strip(),"***\n")
print("Using lstrip()...\n")
print("***",string_2.lstrip(),"***\n")
