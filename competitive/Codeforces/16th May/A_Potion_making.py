size = len
tt = int(input())

for _ in range(tt):
    c = 0
    k = int(input())
    w = 100 - k
    if k == 100:
        c = 1
    elif k == 0:
        c = 1
    elif w >= k:
        if w % k == 0:
            c = w / k
            c += 1
        else:
            c = for_odd(k / 100, w / 100)
    elif k >= w:
        if k % w == 0:
            c = k / w
            c += 1
        else:
            c = for_odd(w / 100, k / 100)
    print(int(c))
