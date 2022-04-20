#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    
    spaces = n-1
    hashes = 1
    
    for i in range(n):
        for x in range(spaces):
            print(' ',end='')
        for x in range(hashes):
            print('#',end='')
        spaces-=1
        hashes+=1
        print()

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
