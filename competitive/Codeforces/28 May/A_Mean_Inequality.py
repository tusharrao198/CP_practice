tt = int(input())
for _ in range(tt):
    n = int(input())
    ans = []
    a = sorted(list(map(int, input().split())))
    l = a[:n]
    r = a[n::]
    r = r[::-1]

    for i in range(n):
        ans.append(l[i])
        ans.append(r[i])
    for j in ans:
        print(j, end=" ")
    print()
