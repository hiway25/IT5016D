#  PerformanceReviews.py
#  Author: Helen Thomas
#  Date: 10.08.2023

#  elif statements

print("Welcome to our performance review program")
rating = float(input("Please input the employees performance rating \n"))
valid_rating = [0.0, 0.4, 0.8]

if rating in valid_rating or rating > 0.8:
    bonus = rating * 2400.00
    print("You have entered", rating, "\n")
    print("This year your bonus is $", bonus, "\n")
    print("Your performance rating is ", end="")

if rating == 0.0:
    print("unacceptable")
elif rating == 0.4:
    print("acceptable")
elif rating >= 0.6:
    print("meritorious")
else:
    print("an invalid rating. Try again")

# Test assertions 1; input 0.4; output $960, acceptable
# Test assertions 2: input 0.1; output; invliad please try again
# Test assertion 3: input 1.0: output; 2400, meritorious
