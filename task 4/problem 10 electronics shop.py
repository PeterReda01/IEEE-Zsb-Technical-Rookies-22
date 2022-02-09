#problem 10 electronics shop
#https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=internal-search

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    max=-1
    keyboards=sorted(keyboards,reverse=True)
    drives=sorted(drives,reverse=True)
    for i in keyboards:
        for j in drives:
            if(i+j<=b):
                max=i+j
                break
    for i in drives:
        for j in keyboards:
            if(i+j<=b):
                if(i+j>max):
                    max=i+j
                    break
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()