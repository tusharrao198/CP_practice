# https://leetcode.com/problems/3sum-closest/submissions//

from typing import *


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = None
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while k > j:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == target:
                    return threeSum
                if closest is None or abs(target - threeSum) < abs(target - closest):
                    closest = threeSum
                if threeSum < target:
                    j += 1
                else:
                    k -= 1
        return closest
