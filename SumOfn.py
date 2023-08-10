#  SumOfn.py
#  Author: Helen Thomas
#  Date: 10.08.2023

n = int(input("Enter a number:  "))
sum = 0
count = 1

while count <= n:
    sum += count
    count += 1

print("The sum of the first", n, "positive integers is:", sum)