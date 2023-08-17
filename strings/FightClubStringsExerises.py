# FightClubStringExercises.py
#  Author: Helen Thomas
#  Date: 17.08.2023

string_1 = "The first rule of fight club: do not talk about fight club."

# Write a program that returns the number of spaces in the string.
spaces_count = string_1.count(" ")

print("The number of times spaces appear is:", spaces_count)

# Returns the number of punctuations (:, . )
def count_punctuation(input_string):
    punctuation_count = 0
    for char in input_string:
        if char in ".:":
            punctuation_count += 1
    return punctuation_count

string_1 = "The first rule of fight club: do not talk about fight club."

total_punctuation = count_punctuation(string_1)

print("The total number of punctuation marks (full stops and colons) is:", total_punctuation)

# Write a program that gets a username from a stored email address. The email address should be a person's first name, followed by a dot, followed by their last name. The username should be the person's last name followed by their first initial. Here is an example test case assertion:
#
# "robert.paulson@hotmail.com" produces the username "paulsonr"
def generate_username(email):
    parts = email.split("@")[0].split(".")
    first_name = parts[0]
    last_name = parts[1]
    username = last_name + first_name[0]
    return username

email_address = "robert.paulson@hotmail.com"
username = generate_username(email_address)

print("Email:", email_address)
print("Username:", username)


#  checks if a given string contains numbers only:
def contains_numbers_only(input_string):
    return input_string.isdigit()

stored_pin = "12345"  # Replace this with your stored pin

if contains_numbers_only(stored_pin):
    print("The stored pin contains numbers only.")
else:
    print("The stored pin does not contain numbers only.")



# takes a list of email addresses, extracts the first names and last names,
# and produces a new list with lists of first names and last names using title case:
def extract_names(email_list):
    names_list = []
    for email in email_list:
        name_parts = email.split("@")[0].split(".")
        first_name = name_parts[0].title()
        last_name = name_parts[1].title()
        names_list.append([first_name, last_name])
    return names_list

list_1 = ["tyler.durden@gmail.com", "marla.singer@yahoo.co.nz"]
list_2 = extract_names(list_1)

for names in list_2:
    print(names)
