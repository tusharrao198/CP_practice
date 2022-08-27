import sys
inp = sys.stdin.readline
n= int(inp())
a=list(map(int, inp().split()))
for i in range(n):
    ans = a.index(i+1)+1
    print(ans, end=" ")