import numpy as np
from itertools import permutations as p 
t = int(input())
for i in range(t):
    s=5
    n = int(input())
    lst = list(map(int, input().split()))
    if n==s:
        print(np.prod(lst))
    elif n>s:
        perm = p(lst)
        lst11=[]
        for j in list(perm):
            print(np.prod(j[:s]))
            lst11.append(np.prod(j[:s]))
        print(list(set(lst11)))
        print(max(lst11))
        


