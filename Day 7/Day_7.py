import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    k = list(map(int,input().split()))

    k.reverse()
    for i in k:
        print(i, end = " ")
