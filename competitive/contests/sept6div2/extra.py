from itertools import permutations as p 

lst = [1,2,3,4,5]
lst1=[(1,2,3),(4,5,6)]
"""
for i in range(len(lst)):
    if i < len(lst)-1:
        a = lst[i]+lst[i+1]
        print(a)

"""
perm = p(lst)
for k in list(perm):
    print(type(k))
for i in lst1:
    for j in i:
        print(j,end=",")
       