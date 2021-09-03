from typing import List

# https://www.programmersought.com/article/3386477469/

# https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmax = float("-inf")
        ans = float("-inf")
        for i in range(len(nums)):
            if curmax <= 0:
                curmax = nums[i]
            else:
                curmax += nums[i]
            print(curmax, ans)
            ans = max(curmax, ans)
        return ans


s = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# arr = [-1]
ans = s.maxSubArray(arr)
print(ans)


