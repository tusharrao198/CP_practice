from typing import List

# https://leetcode.com/problems/combination-sum/submissions/


class Solution:
    def solution(self, candidates, ans, cur, target, index, sum_):
        if sum_ == target:
            ans.append(cur[:])
        elif sum_ < target:
            for i in range(index, len(candidates)):
                cur.append(candidates[i])
                self.solution(candidates, ans, cur, target, i, sum_ + candidates[i])
                cur.pop()
        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(candidates, ans, cur, target, index=0, sum_=0)
        return ans


s = Solution()
ans = s.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
# arr = [2, 3, 6, 7]
# ans = s.combinationSum(arr, 7)
print(ans)
