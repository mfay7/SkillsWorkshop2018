"""
This script implements a solution to Project Euler question #1
by summing all multiples of 3 or 5 under 1000

Author: Meredith Fay
"""

sum = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        sum += x

print(sum)
