def solve(n, lst):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (i + j + 2) == (lst[i] * lst[j]):
                count += 1
    return count


tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = list(map(int, input().split()))
    print(solve(n, lst))
