# Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/
# https://leetcode.com/problems/combination-sum-iii/submissions/

from typing import List

# for combination sum without dup array should be sorted first and then a check if that number is used already or not


class Solution:
    def solution(self, k, candidates, ans, cur, target, index, sum_):
        if sum_ == target and (len(cur[:]) == k):
            ans.append(cur[:])
        elif sum_ < target:
            prev = -1
            for i in range(index, len(candidates)):
                num = candidates[i]
                if prev != candidates[i] and (num % 10 == num):
                    cur.append(candidates[i])
                    self.solution(
                        k, candidates, ans, cur, target, i + 1, sum_ + candidates[i]
                    )
                    # print("cur = ", cur)
                    x = cur.pop()
                    # print("pop = ", x)
                    prev = candidates[i]
                    # print(f"prev= {prev}")
        return

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        cur = []
        candidates = [_ for _ in range(1, 10)]
        self.solution(k, candidates, ans, cur, n, index=0, sum_=0)
        return ans


s = Solution()
ans = s.combinationSum3(3, 7)
print(ans)
