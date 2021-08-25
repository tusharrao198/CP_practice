# size = len
# tt = int(input())
# for _ in range(tt):
#     dC = int(input())
#     a = map(int, input().split())

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'applicationPairs' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER deviceCapacity
#  2. 2D_INTEGER_ARRAY foregroundAppList
#  3. 2D_INTEGER_ARRAY backgroundAppList
#

def applicationPairs(deviceCapacity, foregroundAppList, backgroundAppList):
    # Write your code here
    di = {}
    for f in range(len(foregroundAppList)):
        for b in range(len(backgroundAppList)):
            di[[foregroundAppList[f][0], backgroundAppList[b][0]]] = [backgroundAppList[b][1]+foregroundAppList[f][1]]

    max_ = -1
    desc = sorted([l[1] for l in list(di.values())], reverse=True)
    for ii in desc:
        if ii<=deviceCapacity:
            max_ = ii
            break

    for k, v in di.items():  
        if v[1]==max_:
            return [[k, v[0]]]
    return [[]]
        
deviceCapacity = 7
foregroundAppList = [[1,2], [2,4], [3,6]]
backgroundAppList = [[1,2]]

print(applicationPairs(deviceCapacity, foregroundAppList, backgroundAppList))

# if _name_ == '_main_':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     deviceCapacity = int(input().strip())

#     foregroundAppList_rows = int(input().strip())
#     foregroundAppList_columns = int(input().strip())

#     foregroundAppList = []

#     for _ in range(foregroundAppList_rows):
#         foregroundAppList.append(list(map(int, input().rstrip().split())))

#     backgroundAppList_rows = int(input().strip())
#     backgroundAppList_columns = int(input().strip())

#     backgroundAppList = []

#     for _ in range(backgroundAppList_rows):
#         backgroundAppList.append(list(map(int, input().rstrip().split())))

#     result = applicationPairs(
#         deviceCapacity, foregroundAppList, backgroundAppList)

#     fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
#     fptr.write('\n')

#     fptr.close()
