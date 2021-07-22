from itertools import permutations as p 
t =int(input())
ans =[]
for i in range(t):
    lsta=[]
    n = int(input())
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if j < len(lst)-1:
            a = lst[j]+lst[j+1]
            lsta.append(a)
    
    lst_dup=[]
    perm = p(lst)
    for k in list(perm):
        if list(k)!=lst:
            lstx=[]
            for m in range(len(k)):
                if m < len(k)-1:
                    dup = k[m]+k[m+1]
                    lstx.append(dup)
            if sorted(lstx) == sorted(lsta):
                lst_dup=list(k)
                break        
    
    for xx in lst_dup:
        print(xx,end=" ")

