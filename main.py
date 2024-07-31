#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count_a = 0
    count_b = 0
    
    for i in apples:
        i = a + i   # i == landed_position of apples
        
        if i <= t and i >= s:
            count_a += 1
    for j in oranges:
        j = b + j   # j == landed_position of oranges
        if j >= s and j <= t:
            count_b += 1 

    print(count_a)
    print(count_b)

    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])    # started point of sam's house

    t = int(first_multiple_input[1])    # ended point of sam's house

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])   

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])    # count of apples

    n = int(third_multiple_input[1])    # count of orange

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
