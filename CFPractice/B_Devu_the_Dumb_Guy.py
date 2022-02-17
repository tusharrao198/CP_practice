n, x = map(int, input().split())
chap=list(map(int, input().split()))
chap.sort()
ans = 0
for i in range(n):
    if x>=1:
        ans += (chap[i]*x)
    else:
        ans += (chap[i]*1)
    x-=1
print(ans)
