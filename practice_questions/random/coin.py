# minimum no. of coins required to construct the given sum from a list of given numbers.

tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = list(map(int, input().split()))  # [1,2,5]
    res = [0 for _ in range(n + 1)]
    res[0] = 0
    for i in range(1, n + 1):
        res[i] = float("inf")
        for j in range(len(lst)):
            if i - lst[j] >= 0:
                res[i] = min(res[i], res[i - lst[j]] + 1)
    print(res[n])
