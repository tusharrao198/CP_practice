n= int(input())
b=list(map(int, input().split()))
m= int(input())
g=list(map(int, input().split()))
b.sort()
g.sort()
ans = 0
for i in range(n):
    for j in range(m):
        if g[j]!="T" and abs(b[i]-g[j])<=1:
            ans+=1
            g[j]="T"
            break

print(ans)