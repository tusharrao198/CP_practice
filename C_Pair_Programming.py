tt = int(input())
for _ in range(tt):
    s = input()
    k, n, m = map(int, input().split())
    mono = list(map(int, input().split()))
    poly = list(map(int, input().split()))

    i = j = 0
    ans = []
    while True:
        if i < n and mono[i] <= k:
            if mono[i] == 0:
                k += 1
            ans.append(mono[i])
            i += 1
        elif j < m and poly[j] <= k:
            if poly[j] == 0:
                k += 1
            ans.append(poly[j])
            j += 1
        else:
            break

    if i < n or j < m:
        ans = [-1]

    for i in ans:
        print(i, end=" ")
    print()
