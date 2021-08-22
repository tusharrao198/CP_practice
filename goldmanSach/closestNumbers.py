# https: // www.hackerrank.com/challenges/closest-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def closestNumbers(arr):
    arr.sort()
    n = len(arr)
    _min = float("inf")
    for i in range(1, n):
        diff = abs(arr[i] - arr[i-1])
        _min = min(_min, diff)
    ans = []
    for i in range(1, n):
        if abs(arr[i]-arr[i-1]) == _min:
            ans.append(arr[i-1])
            ans.append(arr[i])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
