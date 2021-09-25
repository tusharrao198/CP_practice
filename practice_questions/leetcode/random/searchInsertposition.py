from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if nums[r]<target:
            return r+1
            
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
        return l

s = Solution()
target = 5
arr = [1, 2, 3, 4, 5, 5, 6]
x = s.searchInsert(arr, target)
print(x)
