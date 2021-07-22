# sliding window technique
def solve(n, k, lst):
    window_sum = sum([lst[_] for _ in range(k)])
    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - lst[i] + lst[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum


tt = int(input())
for _ in range(tt):
    # n, k = map(int, input().split())
    n, k = 4, 2
    # res = map(int, input().split())
    res = [80, -50, 90, 100]
    print(solve(n, k, res))
