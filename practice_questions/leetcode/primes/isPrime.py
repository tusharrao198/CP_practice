import math

class Solution:
    # @param A : integer
    # @return an integer

    def isPrime(self, A):
        if A == 1:
            return 0
        if A == 2:
            return 1
        if A == 3:
            return 1
        for i in range(2, int(math.sqrt(A)) + 1):
            if A % i == 0:
                return 0
        return 1

S = Solution()
ans = S.isPrime(83)
print(ans)