import sys
inp = sys.stdin.readline
n= int(inp())
a=list(map(int, inp().split()))
b=list(map(int, inp().split()))

s = set()
for i in range(1, a[0]+1):
    s.add(a[i])
for i in range(1, b[0]+1):
    s.add(b[i])

# print(s)
f = False
for i in range(1,n+1):
    if i not in s:
        # print(i)
        f=True
        break
if not f:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
