def inc_sub(lst):
    length = [1 for _ in range(len(lst))]
    for i in range(len(lst)):
        length[i] = 1
        for j in range(i):
            if lst[j] < lst[i]:
                length[i] = max(length[i], length[j] + 1)
    return max(length)


tt = int(input())
for _ in range(tt):
    n = int(input())
    res = inc_sub(list(map(int, input().split())))
    print(res)
