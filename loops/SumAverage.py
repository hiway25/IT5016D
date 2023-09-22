# SumAverage.py
#  Author: Helen Thomas
# Date: 11.08.2023

# Initialize variables to keep track of the sum and count of numbers
total_sum = 0
count = 0

# Get input from the user and process until 0 is entered
while True:
    num = int(input("Enter an integer (enter 0 to finish): "))

    # Check if the user entered 0 to finish
    if num == 0:
        break

    # Increment the count and add the number to the total sum
    count += 1
    total_sum += num

# Calculate the average if there are numbers entered
if count > 0:
    average = total_sum / count
    print("Sum:", total_sum)
    print("Average:", average)
else:
    print("No numbers entered.")
