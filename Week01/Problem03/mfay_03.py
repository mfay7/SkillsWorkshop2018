"""
This function implements a solution to project Euler question #3
by finding the largest prime factor of any number, but specifically 600851475143

Used help from stack overflow

Author: Meredith Fay
"""

def largestprimefactor(n):

    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1

    print(n)
        
largestprimefactor(600851475143)
