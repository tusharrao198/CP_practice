# https://leetcode.com/problems/combination-sum-iv/
# for combination sum without dup array should be sorted first and then a check if that number is used already or not

# Explanation
# https://dev.to/seanpgallivan/solution-combination-sum-iv-3620


# Not completed yet tle case

from typing import List


class Solution:
    def solution(self, nums, ans, cur, target, sum_):
        if sum_ == target:
            ans.append(cur[:])

        elif sum_ < target:
            for i in range(len(nums)):
                cur.append(nums[i])
                self.solution(nums, ans, cur, target, sum_ + nums[i])
                cur.pop()
        return

    def combinationSum4(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(nums, ans, cur, target, sum_=0)
        return len(ans)


s = Solution()
# ans = s.combinationSum4([10, 1, 2, 7, 6, 1, 5], 8)
ans = s.combinationSum4([1, 2, 3], 4)
# ans = s.combinationSum4([4, 2, 1], 32) # TLE case
print(ans)
