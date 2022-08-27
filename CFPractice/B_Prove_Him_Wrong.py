import sys
inp = sys.stdin.readline
for vv in range(int(inp())):
    n= int(inp())
    if n>19: print("NO")
    else:
        print("YES")
        print(*[3**i for i in range(n)])
