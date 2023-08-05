import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = f"{n:b}"
    seg = binary.split("0")
    seg_len = map(len, seg)
    max_l = max(seg_len)

    print(max_l)
