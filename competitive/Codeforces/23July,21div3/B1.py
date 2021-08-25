tt = int(input())
for _ in range(tt):
    s = input()
    dd = {}
    for i in s:
        dd[i] = dd.get(i, 0) + 1
    dd = {k: v for k, v in sorted(dd.items(), key=lambda x: -x[1])}
    countr = 0
    countg = 0
    count1 = 0
    for k, v in dd.items():
        if v >= 2:
            countr += 1
            countg += 1
        elif v == 1:
            count1 += 1
    countr += count1 // 2
    countg += count1 // 2
    print(countr)








