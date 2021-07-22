tt = int(input())
for _ in range(tt):
    lst = list(map(int, input().split()))
    lstd = sorted(lst, reverse=True)[:2]
    lhs = lst[:2]
    rhs = lst[2:]
    mxl = max(lhs)
    mxr = max(rhs)
    if (mxl in lstd) and (mxr in lstd):
        print("YES")
    else:
        print("NO")
