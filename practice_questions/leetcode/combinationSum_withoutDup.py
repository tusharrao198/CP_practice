from typing import List

# for combination sum without dup array should be sorted first and then a check if that number is used already or not


class Solution:
    def solution(self, candidates, ans, cur, target, index, sum_):
        if sum_ == target:
            ans.append(cur[:])

        elif sum_ < target:
            prev = -1
            for i in range(index, len(candidates)):
                if prev != candidates[i]:
                    cur.append(candidates[i])
                    self.solution(
                        candidates, ans, cur, target, i + 1, sum_ + candidates[i]
                    )
                    # print("cur = ", cur)
                    x = cur.pop()
                    # print("pop = ", x)
                    prev = candidates[i]
                    # print(f"prev= {prev}")
        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        candidates.sort()
        self.solution(candidates, ans, cur, target, index=0, sum_=0)
        return ans


s = Solution()
ans = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 10)
print(ans)
