# https://www.youtube.com/watch?v=FtiWd8PIpxI

import math
n=int(input())
arr = list(map(int, input().split()))
# 1  0 0  1 0
# converted to 
# -1 1 1 -1 1
x=0
can_be_flipped=0
cnt1=0
for i in range(n): # kadane's algo
    if arr[i]==0:
        x= max(0, x + 1)
    else:
        x= max(0, x+(-1))
        cnt1+=1
    can_be_flipped = max(x, can_be_flipped)
    
out = can_be_flipped + cnt1
if cnt1==n:
    print(out-1)
else:
    print(out)