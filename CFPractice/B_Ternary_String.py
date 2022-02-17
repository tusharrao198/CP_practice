for _ in range(int(input())):
    st = [int(i) for i in list(input())]
    n= len(st)

    a = [[st[0]]]
    r = 0
    for i in range(1, n):
        if st[i-1]==st[i]:
            a[r].append(st[i])
        else:
            a.append([st[i]])
            r+=1
    print(a)
