from typing import *

# https: // leetcode.com/problems/third-maximum-number/ 

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) == 3:
            return min(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            i = 1
            while i < 3:
                nums.remove(max(nums))
                i += 1
        return max(nums)
