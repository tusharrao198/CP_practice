from math import log2

class Solution:
    mem = {1:1}
    def solve (self, n):
        if n in Solution.mem:
            return Solution.mem[n]
        start = max(Solution.mem.keys())
        res = Solution.mem[start]
        for i in range(start+ 1, n+1):
            res <<= int(log2(i)) +1
            res +=i
            res %= 1000000007
            Solution.mem[i] = res
        return res

    def concatenatedBinary(self, n: int) -> int:
        return self.solve(n)
