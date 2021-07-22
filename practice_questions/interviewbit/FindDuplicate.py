from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()  # sort array in O(nlogn) time
        for i in range(1, len(nums)):  # traverse in O(n)
            if nums[i] == nums[i-1]:
                return nums[i]

# Total time = O(nlogn)