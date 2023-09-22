# MultiplesLoop.py
#  Author: Helen Thomas
#  Date: 10.08.2023

# Write a program that prints multiples of p from 10 until the value of q (inclusive)
# the user enters: p = 4   and    Q = 29     Answer: 12, 16, 20, 24, 28,

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))

output = "Multiples of " + str(p) + " from 10 to " + str(q) + " are: "

current = 10
multiples = []

while current <= q:
    if current % p == 0:
        multiples.append(str(current))
    current += 1

output += ", ".join(multiples)
print(output)
