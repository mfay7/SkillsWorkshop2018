"""
This script implements a solution to project Euler question #2
by summing all even Fibonacci numbers whose values do not exceed four million

Author: Meredith Fay
"""

fibonacci_1 = 1
fibonacci_2 = 2
count = 0

while (fibonacci_1 <= 4e6):
    fibonacci_update = fibonacci_1 + fibonacci_2
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_update

    if fibonacci_1 % 2 == 0:
        count += fibonacci_1

print(count)
