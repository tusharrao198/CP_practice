from typing import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        ans = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                counter += 1
            else:
                counter=0
            ans = max(ans, counter)
            i += 1
        return ans


s = Solution()
arr = [1, 1, 0, 1, 1, 1]
x = s.findMaxConsecutiveOnes(arr)

print(x)