"""
This script implements a solution to project Euler question #5
by finding the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20

Used help from stack overflow

Author: Meredith Fay
"""

i = 1
for k in (range(1, 21)): 
  if i % k > 0: 
    for j in range(1, 21): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print(i)
