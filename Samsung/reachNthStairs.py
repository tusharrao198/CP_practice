# count the number of ways to reach n'th stair when
# user climb 1 .. m stairs at a time.


def countWays(n, m):
    tmp = 0
    ans = [1]
    for i in range(1, n + 1):
        s = i - m - 1
        e = i - 1
        if s >= 0:
            tmp -= ans[s]
        tmp += ans[e]
        ans.append(tmp)

    return ans[n]


# Driver Code
n = 5
m = 3  # no. of stairs

print("Number of ways =", countWays(n, m))
