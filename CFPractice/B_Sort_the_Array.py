import sys
inp = sys.stdin.readline
n= int(inp())
arr=list(map(int, inp().split()))

l = 0
r = 0

for i in range(n-1):
    if arr[i]>arr[i+1]:
        l=i
        # print(l)
        break

for i in reversed(range(1, n)):
    if arr[i-1]>arr[i] and l<=i:
        r = i
        # print(r)
        break

ans = []
tmp = []
for i in range(l):
    tmp.append(arr[i])

for i in reversed(range(l,r+1)):
    ans.append(arr[i])
tmp.extend(ans)

for i in range(r+1, n):
    tmp.append(arr[i])

a=sorted(arr)
# print(a, tmp, l, r)
if a==tmp and l<=r:
    print('yes')
    print(l+1, r+1)
else:
    print("no")
