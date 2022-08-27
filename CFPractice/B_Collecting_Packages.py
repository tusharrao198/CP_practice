import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    lst = [[0,0]]
    for __ in range(n):
        x, y = map(int, inp().split())
        lst.append([x,y])
    
    lst.sort(key=lambda x: (x[0], x[1]))

    s = ""
    fnd = False
    for i in range(1, n+1):
        r = lst[i][0] - lst[i-1][0]
        u = lst[i][1] - lst[i-1][1]
        if r<0 or u<0:
            fnd = True
            break
        s = s + ("R"*r)
        s = s + ("U"*u)
        # print("AA = ", s)
    if not fnd:
        print("YES")
        print(s)
    else:
        print("NO")