from collections import Counter


def make_ans(f, a):
    cf = Counter(f)
    for x in a:
        cf[x] -= 1
    b = []
    for k, v in cf.items():
        b += [k] * v
    b.sort()
    return [a, b]


class Solution:
    def avgset(self, A):
        A.sort()
        s, n = sum(A), len(A)

        dp = [{0: []}]

        MAXL = n // 2

        for x in A:
            if len(dp) < MAXL + 1:
                dp.append({})

            for i in range(len(dp) - 1, 0, -1):
                for k, v in dp[i - 1].items():

                    if (k + x) * n <= s * i:
                        t = v + [x]

                        if k + x not in dp[i] or t < dp[i][k + x]:
                            dp[i][k + x] = t

            if len(dp[-1]) == 0:
                dp.pop()

        for i in range(1, len(dp)):
            if s * i % n != 0:
                continue
            si = s * i // n
            if si in dp[i]:
                return make_ans(A, dp[i][si])

        return []
