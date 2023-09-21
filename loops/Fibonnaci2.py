#  Fibonacci2.py
#  Author: Helen Thomas
#  Date: 11.08.2023

#  code below if run is very slow because of the way the computer is being asked to calculate
#   bottom code uses Memoization to fix this.

'''
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
    print(n, ":", fibonacci(n))

    '''

fibonacci_cache = {}

def fibonacci(n):
    # If we have the value cached, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 101):
    print(n, ":", fibonacci(n))

