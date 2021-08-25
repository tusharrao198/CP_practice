import math 
tt = int(input())
for _ in range(tt):
    x = int(input())
    a = 2**math.floor(math.log(x,2))
    print(a-1)
    