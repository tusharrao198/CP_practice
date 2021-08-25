N, M, K = list(map(int, input().split()))
count=0
dict ={}
lst_x =[]
for i in range(N):
    lst = list(map(int, input().split()))
    lst_x.append(lst)
    dict[lst[0]] = dict.get(lst[0],0) +1
    
lst1 = list(dict.values())
m  =max(lst1)
ind = lst1.index(m)
a = list(dict.keys())[ind]
print(dict)
print(a)        
lst_index=[]
for x in range(len(lst_x)):
    if K in lst_x[x]:
        index_k = lst_x[x].index(K)
        for i in range(index_k):
            ss = lst_x[x][i]
            lst_index.append(ss)
print(lst_index)

sd = set(lst_index)
print(len(list(sd)))


