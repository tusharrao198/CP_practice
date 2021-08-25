size = len
tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = list(map(int, input().split()))
    d = {}
    pos = []
    for i in range(size(lst)):
        pos.append(lst[i]-(i+1))
    for j in pos:
        d[j] = d.get(j, 0) + 1
    
    count =0
    for k in d.values():
        if k!=1:
            count += k*(k-1)//2
    print(count)

