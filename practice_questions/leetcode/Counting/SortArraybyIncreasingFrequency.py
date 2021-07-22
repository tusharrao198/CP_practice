from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dd = {}
        for i in nums:
            dd[i] = dd.get(i, 0) + 1

        # sorted w.r.t frequency increasing order and then in decreasing order based on second lambda (x[0])
        # " - " in lambda indicate sorting in descending order
        dd = {k: v for k, v in sorted(dd.items(), key=lambda x: (x[1], -x[0]))}
        lst = []
        for i in list(dd.keys()):
            lst.extend([i] * dd[i])
        return lst


# https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/