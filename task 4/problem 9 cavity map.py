#problem 9 cavity map
#https://www.hackerrank.com/challenges/cavity-map/problem?h_r=internal-search

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    print(grid)
    alls=[]
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            if(int(grid[i][j])>int(grid[i+1][j])
            and int(grid[i][j])>int(grid[i-1][j])
            and int(grid[i][j])>int(grid[i][j+1])
            and int(grid[i][j])>int(grid[i][j-1])):
                alls.append((i,j))
    for pair in alls:
        temp=[]
        temp=list(grid[pair[0]])
        temp[pair[1]]="X"
        grid[pair[0]]="".join(temp)
    return grid

if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print(result)
