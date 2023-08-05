import math
import os
import random
import re
import sys

def hourglass (array,n,m):
    total=0
    for i in range(m,m+3):
        total += array[n][i]
        total += array[n+2][i]
    total += array[n+1][m+1]
    return total
        

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

maxi=hourglass(arr,0,0)# Matrix can contein negative values
             
for i in range(4):
        for j in range(4):
            if hourglass(arr,i,j)>maxi:
                maxi = hourglass(arr,i,j)
                    
print(maxi)