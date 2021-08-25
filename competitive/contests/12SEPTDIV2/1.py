t = int(input())

def fun(lst):   # for smallest non neg int
    lst1 = [i for i in range(len(lst))]
    for j in lst1:
        if j not in lst:
            return j
        else:
            continue

def splitting(lst):
    lsta = []
    lstb=[]
    lstxx = []
    for i in set(lst):
        if lst.count(i)==1:
            lsta = lst
            return lsta,lstb
        elif lst.count(i)>1:
            for kk in range(lst.count(i)):
                lsta.append(i)
                lst.remove(i)
                lstb.append(i)
                lst.remove(i)
            #for x in range(len(lst)/2)
            #if lst.count(i)==(lsta.count(i)+lstb.count(i)):
                
    for k in set(lst):
        if k not in 
        
    



        
            

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    