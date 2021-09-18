# https://leetcode.com/problems/k-closest-points-to-origin/submissions/

from math import sqrt
import heapq as hp
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        for x, y in points:
            dist = sqrt(x * x + y * y)
            hp.heappush(lst, [dist, x, y])

        ans = []
        for i in range(k):
            aa = hp.heappop(lst)
            ans.append([aa[1], aa[2]])
        return ans


s = Solution()
arr = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(s.kClosest(arr, k))
