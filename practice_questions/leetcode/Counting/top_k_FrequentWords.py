class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dd = {}
        for i in words:
            dd[i] = dd.get(i, 0) + 1

        dd = {k: v for k, v in sorted(dd.items(), key=lambda x: (-x[1], x[0]))}
        keyss = list(dd.keys())

        lst = []
        for i in range(k):
            lst.append(keyss[i])

        return lst

# https://leetcode.com/problems/top-k-frequent-words/submissions/
#
# Runtime: 52 ms, faster than 90.63% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14.6 MB, less than 11.55% of Python3 online submissions for Top K Frequent Words.
