from math import inf
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    min_len = float("inf")
    cur = 0
    i = 0
    l = 0
    while i < len(nums):
        cur += nums[i]

        while cur >= target:
            min_len = min(min_len, i + 1 - l)
            cur -= nums[l]
            l += 1
        i += 1

    if min_len == inf:
        return 0
    return min_len


lst = [2,3,1,2,4,3]
# lst = [1, 1, 1, 1, 1, 1, 1, 1]
target = 7
print(minSubArrayLen(target, lst))
