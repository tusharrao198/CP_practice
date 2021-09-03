# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}

        for i in range(1, len(nums)+1):
            d[i] = 0

        for i in nums:
            d[i] += 1

        x, y = 0, 0
        for k, v in d.items():
            if d[k] == 2:
                x = k
            elif d[k] == 0:
                y = k
        return [x, y]
