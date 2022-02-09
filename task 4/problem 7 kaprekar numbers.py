#problem 7 modified laprekar numbers
#https://www.hackerrank.com/challenges/kaprekar-numbers/problem?h_r=internal-search

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    r=0
    l=0
    count=False
    while(p<=q):
        r=str(p**2)[-len(str(p)):]
        l=str(p**2)[:len(str(p**2))-len(str(p))]
        if(p==(int(r or 0)+int(l or 0))):
            print(p,end=" ")
            count=True
            p+=1
        else:
            p+=1
    if(count==False):
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
