import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n, m = map(int, inp().split())
    x = ((m-1)%2!=0 and (n-1)%2==0) or ((n-1)%2!=0 and (m-1)%2==0)
    if x: print("Burenka")
    else: print("Tonya")