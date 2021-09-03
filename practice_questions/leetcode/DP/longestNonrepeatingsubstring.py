def solve(s):
    d = {}
    n = len(s)
    l = 0  # left
    ans = 0
    r = 0  # right
    while l < n and r < n:
        val = s[r]
        if val in d:
            l = max(l, d[val] + 1)
        d[val] = r
        print(f" d = {d} =============================== l = {l} and r = {r}")
        ans = max(ans, abs(r - l) + 1)
        r += 1
    return ans


# tt = int(input())
tt = 1
for _ in range(tt):
    # n, k = map(int, input().split())
    # res = map(int, input().split())
    res = ["abcabcbb", "bbbbb", "pwwkew", "", "aab"]
    # for i in res:
    print(solve(res[-3]))
