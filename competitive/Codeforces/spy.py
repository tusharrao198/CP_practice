t = int(input())
for i in range(t):
    d = {}
    n = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    for i in lst:
        d[i] = d.get(i, 0) + 1
    for k ,v in d.items():
        if v==1:
            print(lst.index(k)+1)
