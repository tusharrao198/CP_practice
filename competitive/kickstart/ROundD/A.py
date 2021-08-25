def solve(ss, others):
    dd = {}
    for i in range(len(ss)):
        f = ss[i][0] + ss[i][1]
        if f % 2 == 0:
            mid = f//2
            dd[mid] = dd.get(mid, 0) + 1

    dd = sorted(dd.items(), key=lambda x: x[1])
    max_=0
    if len(dd)!=0:    
        max_ = dd[len(dd)-1][1]    
    for j in range(len(others)):
        if (others[j][0] > others[j][1] > others[j][2]):
            if ((others[j][0]+others[j][2]) == 2*others[j][1]):
                max_+=1

        elif others[j][0] < others[j][1] < others[j][2]:
            if ((others[j][2]+others[j][0]) == 2*others[j][1]):
                max_+=1

        elif others[j][0] == others[j][1] == others[j][2]:
            max_ += 1
    return max_

tt = int(input())
for _ in range(tt):
    a0, a1, a2 = map(int, input().split())
    b0, b2 = map(int, input().split())
    c0, c1, c2 = map(int, input().split())

    ss = [[a0, c2], [a1, c1], [a2, c0], [b0, b2]]
    others = [[a0, b0, c0], [a2, b2, c2], [a0, a1, a2], [c0, c1, c2]]
    ans = solve(ss, others)
    print(f"Case #{_+1}: {ans}")
