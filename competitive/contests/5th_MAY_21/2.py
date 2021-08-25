size = len
tt = int(input())


def check(s):
    c = 1
    v = str(s)
    same = v[0]
    for g in range(1, len(v)):
        if v[g] == same:
            c += 1
        else:
            break
    if c == len(v):
        return True
    else:
        return False


for _ in range(tt):
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if len(str(i)) == 1:
            count += 1
        else:
            if check(i):
                count += 1
    print(count)
