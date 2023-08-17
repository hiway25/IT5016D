# FibonnaciUsingWhile.py
#  Author: Helen Thomas
#  Date: 11.08.2023

print("\nThe Fibonacci Sequence:\n")

p = int(input("Please enter a number corresponding to the position of the sequence (should be at least 3:)"))
q = int(input("Please enter number of terms to generate (should be a positive integer):  "))

print("\n", q, "numbers in the sequence starting from term ", p, ":")

#  initialise counters to zero
p_counter, q_counter = 2, 0

# initialise the first two terms in sequence
n1, n2 = 0, 1

while q_counter < q:
    nth = n1 + n2
    n1, n2 = n2, nth
    p_counter += 1
    if p_counter >= p:
        q_counter += 1
        if q_counter < q:
            print(nth, end =", ")
        else:
            print(nth)

'''
Test assertions 1; 3 numbers from 8 = 13, 21, 34
Test assertion 2: 9 numbers from 5 = 21, 34, 55, 89, 144'''
