# NZQuiz.py
# Author: Helen Thomas
# Date: 09.08.2023

# Activity challenge 2
# Do some research online and find out 5 interesting facts about New Zealand that you never knew.
# Make these into 5 quiz questions. These can be multiple choice, short answers or both.
# Use Python to create the quiz.
# At the end of the quiz, the user should be presented with their score.
# A good program will not be case sensitive.
# An excellent program will display the total time taken to complete the quiz.

import time

# Get start time
start_time = time.time()

score = 0  # initialise the score

#  Question 1 - multi choice
print("What is the Capital of New Zealand?")
print("A: Auckland.")
print("B: Wellington.")
print("C: Dunedin.")
print("D: Rotorua.")
answer1 = input("Please enter your answer  \n")

if answer1 != 'B' and answer1 != 'b':
    print("Your answer is incorrect.  The correct answer is B: Wellington  \n")
else:
    print("Correct!  \n")
    score += 1

#  Question 2 - True or False
print("True or False?  New Zealand has more sheep than people? \n")
answer2 = input("T/F \n")

if answer2 == "T" or answer2 == "t":
    print("Correct! There are 10 sheep for every person in NZ  \n")
    score += 1
else:
    print("Incorrect.  There are 10 sheep for every person in NZ  \n")

# Question 3
print("In which NZ city will you find the worlds steepest street?  \n")
answer3 = input("Please type your answer  \n").lower()

if answer3 == "dunedin":
    print("Correct!  Baldwin Street in Dunedin is a crazy 19 degree slope  \n")
    score += 1
else:
    print("Incorrect.  Baldwin Street in Dunedin is a crazy 19 degree slope \n")

#  Question 4
print("What body of water is to the East of NZ?")
print("A: Pacific Ocean.")
print("B: Tasman Sea.")
print("C: Southern Ocean.")
print("D: Atlantic Ocean.")
answer4 = input("Please enter your answer  \n").lower()

if answer4 != 'a':
    print("Your answer is incorrect.  The correct answer is A: Pacific Ocean  \n")
else:
    print("Correct!  \n")
    score += 1

#  calculate time taken
end_time = time.time()
time_taken = end_time - start_time

print("Quiz completed  \n")
print("Total score:", score, "/4  \n")
print("Time taken:", time_taken, "seconds")
