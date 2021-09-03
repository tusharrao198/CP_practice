# boats to save
def solve(n, lst):
    # using two pointer technique
    print(f"lst = {lst}")
    l = 0  # left
    r = len(lst) - 1  # right
    count = 0
    while l <= r:
        # print(f"lst[l] + lst[r] = {lst[l] + lst[r]} and n = {n}")
        if l == r:
            count += 1
            break
        if (lst[l] + lst[r]) <= n:
            l += 1
        r -= 1
        count += 1
        # print(f" r = {r} and l = {l} and count = {count}")
    return count


tt = int(input())
for _ in range(tt):
    # n, k = map(int, input().split())
    # res = map(int, input().split())
    n = 3
    res = [1, 3, 2, 3]
    print(solve(n, sorted(res)))
