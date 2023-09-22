#  MultiplicationTable
#  Author: Helen Thomas
#  Date: 11.08.2023

num = int(input("Enter a number: "))

# create muliplication table
print("Multiplication table for ", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
