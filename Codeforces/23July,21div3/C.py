tt = int(input())
for _ in range(tt):
    n = int(input())
    # lsts = []
    s = ""
    for i in range(n):
        xx = input()
        s += xx
        # lsts.append(xx)
    dd = {}
    for i in s:
        dd[i] = dd.get(i, 0) + 1
    dd = {k: v for k, v in sorted(dd.items(), key=lambda x: -x[1])}
    print(dd)
    vals = list(dd.values())
    print(vals)
    if len(vals) == 1:
        print(0)
    elif len(vals) > 1:
        if vals[0] > vals[1]:
            if vals[0] - sum(vals[1:]) >0:
                print(n)
            else:
                print(n-1)
        elif vals[0] == vals[1]:
            print(0)
    else:
        print(0)
