#problem 5 find digits
#https://www.hackerrank.com/challenges/find-digits/problem?h_r=internal-search

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    count=0
    for divisor in str(n):
        if(int(divisor)==0):
            continue
        if(n%int(divisor)==0):
            count+=1
    return int(count)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
