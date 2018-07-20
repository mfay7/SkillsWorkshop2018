"""
This script implements a solution to project Euler question #4
by finding the largest palindrome that is the product of two 3-digit numbers

Author: Meredith Fay
"""

palindromes = []

for x in range(999, 99, -1):

    for y in range(999, 99, -1):

        product = x * y

        if str(product) == str(product)[::-1]:

           palindromes.append(product)

print(max(palindromes))



        
