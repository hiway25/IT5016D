#  Fibonacci2.py
#  Author: Helen Thomas
#  Date: 11.08.2023

#  code below if run is very slow because of the way the computer is being asked to calculate
#   bottom code uses Memoization to fix this.


from functools import lru_cache


@lru_cache(maxsize=1000)

def fibonacci(n):
    #  check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

# compute the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for n in range(1, 501):
    print(n, ":", fibonacci(n))
