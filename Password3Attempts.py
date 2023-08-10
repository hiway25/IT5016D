#  Password3Attempts.py
#  Author: Helen Thomas
#  Date: 10.08.2023

max_attempts = 3
password = "secretpassword"

for attempt in range(max_attempts):
    user_input = input("Enter the password: ")

    if user_input == password:
        print("Access granted.")
        break
    elif user_input.lower() == "exit":
        print("Exiting the program.")
        break
    else:
        remaining_attempts = max_attempts - (attempt + 1)
        if remaining_attempts > 0:
            print("Incorrect password. You have", remaining_attempts, "attempt(s) remaining.")
        else:
            print("Access denied. No attempts remaining.")
