#  LoginDict.py
#  Author: Helen Thomas
#  Date: 14.08.2023

# A stored dictionary has 3 login credentials.
#  Each credential consists of a unique username and a password.

# Define the stored login credentials as a dictionary
credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Initialize the number of login attempts
attempts = 0

print("Welcome to the Login Program!")
print("You have 3 attempts to log in.")

# Loop to handle login attempts
while attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered credentials match the stored credentials
    if username in credentials and credentials[username] == password:
        print("Login successful. Welcome, {}!".format(username))
        break
    else:
        print("Login failed. Please try again.")
        attempts += 1

# Check if all attempts are used
if attempts == 3:
    print("You have reached the maximum number of login attempts. Access denied.")
else:
    print("Thank you for using the Login Program.")
