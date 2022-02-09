#problem 6 Chocolate feast
#https://www.hackerrank.com/challenges/chocolate-feast/problem?h_r=internal-search

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    sum=0
    bought=0
    bought=n//c
    sum=bought
    while(bought//m!=0):
        wrappers=bought//m
        sum+=wrappers
        wrappers=bought//m+bought%m
        bought=wrappers
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
