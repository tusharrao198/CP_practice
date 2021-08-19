import heapq
from typing import List
# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        ksmallest = n - k + 1
        i = 0
        ans = -1
        while i < ksmallest:
            ans = heapq.heappop(nums)
            i+=1
        return ans


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        ksmallest = n - k + 1

        if ksmallest >= n:
            return heapq.nlargest(k, nums)[-1]

        else:
            return heapq.nsmallest(ksmallest, nums)[-1]


s = Solution()
arr = [3,2,1,5,6,4]
arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k =4
print(s.findKthLargest(arr, k))
