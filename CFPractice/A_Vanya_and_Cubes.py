n= int(input())
a = []
c = 0
m = 0
for i in range(1, 10**4//4):
    c = c + i
    a.append(c)
    m+=1

ans = 0
sm = 0
for i in range(m):
    if sm+a[i]<=n:
        ans = i
        sm+=a[i]
print(ans+1)

    