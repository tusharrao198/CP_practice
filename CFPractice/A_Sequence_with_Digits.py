def solve(x):
    mx=float("-inf")
    mn=float("inf")
    for i in str(x):
        num=int(i)
        mx=max(mx,num)
        mn=min(mn,num)

    return mx*mn


tt = int(input())
for _ in range(tt):
    a1, k = map(int, input().split())
    for i in range(k-1):
        out=solve(a1)
        if out==0:
            break
        a1 = a1 + out
    print(a1)
