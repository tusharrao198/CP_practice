# /usr/bin/python3

# approached using backtracking recursively
# https://leetcode.com/problems/subsets/   without duplicates
# and
# https://www.interviewbit.com/problems/subset/

from typing import List


class Solution:
    def solve(self, nums, ans, cur, index):
        if index > len(nums):
            return
        # print(f"cur = {cur}")
        ans.append(cur[:])
        # print(f"ans = {ans}")
        for i in range(index, len(nums)):
            # print(f"i = {i} and nums[i] = {nums[i]}")
            if nums[i] not in cur:
                cur.append(nums[i])
                # print(f"{nums, ans, cur, i}")
                self.solve(nums, ans, cur, i)
                x = cur.pop()
                # print(f"pop = {x}")
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        nums.sort()
        self.solve(nums, ans, cur, 0)
        return ans


s = Solution()
# nums = [1,2,2]
nums = [12, 13]
nums = [15, 20, 12, 19, 4]
ans = s.subsets(nums)
print(ans)
