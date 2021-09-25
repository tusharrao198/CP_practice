# https://leetcode.com/problems/find-k-closest-elements/submissions/
import heapq as hp
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        lst = []

        for i in range(len(arr)):
            hp.heappush(lst, [abs(arr[i] - x), arr[i]])

        ans = []
        for i in range(k):
            ans.append(hp.heappop(lst)[1])

        ans.sort()
        return ans


s = Solution()
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(s.findClosestElements(arr, k, x))
