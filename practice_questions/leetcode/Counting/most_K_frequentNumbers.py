class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = {}
        for i in nums:
            dd[i] = dd.get(i, 0) + 1

        dd = {kk: v for kk, v in sorted(dd.items(), key=lambda item: item[1])}
        keys = list(dd.keys())

        # print(keys)
        lst = []
        ll = len(keys)
        for i in range(k):
            lst.append(keys[ll - i - 1])

        return lst


# https://leetcode.com/problems/top-k-frequent-elements/submissions/