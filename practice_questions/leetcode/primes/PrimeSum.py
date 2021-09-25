from typing import List
import math


class Solution:
    def primesum(self, A: int) -> List[int]:
        arr = self.countPrimes(A)
        # return arr
        pos = []
        n = len(arr)
        i = 2
        j = n - 1
        while i <= j:
            print(i, j)
            if not arr[i]:
                i += 1
            elif not arr[j]:
                j -= 1
            else:
                val = i + j
                if val == A:
                    pos.append(i)
                    pos.append(j)
                    return pos
                elif val < A:
                    i += 1
                elif val > A:
                    j -= 1
        return pos

    def countPrimes(self, n: int) -> List[int]:
        if n < 2:
            return [0]
        arr = [True for _ in range(n)]
        arr[0] = arr[1] = False
        for i in range(2, math.ceil(math.sqrt(n))):
            if arr[i]:  # True
                for j in range(i ** 2, n, i):  # multiples of i set to False
                    arr[j] = False
        return arr


s = Solution()
A = 1048574
A = 4

x = s.primesum(A)
print(x)
