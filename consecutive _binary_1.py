'''
Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    count1 = 0
    count2 = 0

    while n:
        if n & 1:
            count1 +=1
        else:
            if (count1 != 0):
                if (count2 < count1):
                    count2 = count1
            count1 = 0
        n >>= 1
                
    if (count1 > count2):
        print(count1);
    else:
        print(count2)

