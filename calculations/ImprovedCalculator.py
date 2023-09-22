# ImprovedCalculator.py
# Author: Helen Thomas
# Date: 18.08.2023

def do_calculation(user_input):

    # variable to store result
    calculated_answer = int

    #Split the input
    split_input = user_input.split()

    # get the parameters from split_input
    input_params = split_input[1].split(",")

    #do if elif

    if split_input[0] =="add":
        calculated_answer = int(input_params[0]) + int(input_params[1])
    elif split_input[0] == "subtract":
        calculated_answer = int(input_params[0]) - int(input_params[1])
    else:
        return "Unknown command entered!"
    return calculated_answer

#program run code

#getting the input
user_input = input("Please enter an operation and 2 parameters...\n")
# do calculation
print("The answer is: {0}".format(do_calculation(user_input)),
      "\n")
