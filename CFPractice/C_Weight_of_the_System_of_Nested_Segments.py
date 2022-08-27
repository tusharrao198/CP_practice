import sys    
inp = sys.stdin.readline
for _ in range(int(inp())):
    input()
    n, m = map(int, input().split())
    lst = []
    idx = {}
    for i in range(m):
        cord, wt = map(int, inp().split())
        lst.append([cord, wt])
        idx[cord] = i+1
    lst.sort(key=lambda x:(x[1], x[0]))
    lst = lst[:2*n]
    sm = 0
    for i in range(2*n):
        sm+=lst[i][1]
    print(sm)
    # print(idx)
    lst.sort(key=lambda x: x[0])
    ans = []
    for i in range(n):
        print(idx[lst[i][0]], idx[lst[2*n-i-1][0]])
    print()
