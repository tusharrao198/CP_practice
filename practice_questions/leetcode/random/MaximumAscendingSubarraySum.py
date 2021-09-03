from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        c = 0
        max_ = s
        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                s += nums[i]
            else:
                s = nums[i]
            max_ = max(max_, s)
        return max_


s = Solution()

arr = [10, 20, 30, 5, 10, 50]
x = s.maxAscendingSum(arr)
print(x)
