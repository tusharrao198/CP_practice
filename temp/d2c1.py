# town problem

tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = []
    s = 0
    for i in range(n):
        m1, m2 = map(int, input().split())
        s += m1
        lst.append([m1, m2])

    lst.sort(key=lambda x: (-x[0], -x[1]))
    print(lst)

    cnt = 0
    x = 0
    s -= x
    for i in range(n):
        x += lst[i][0] + lst[i][1]
        print(x, s, s - x)
        if x <= s:
            cnt += 1
            s -= lst[i][0]
        else:
            break
    print(cnt)
