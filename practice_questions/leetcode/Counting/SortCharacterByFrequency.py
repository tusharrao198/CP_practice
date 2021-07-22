class Solution:
    def frequencySort(self, s: str) -> str:
        dd = {}
        for i in s:
            dd[i] = dd.get(i, 0) + 1

        dd = {k: v for k, v in sorted(dd.items(), key=lambda x: x[1], reverse=True)}

        sss = ""
        for k, v in dd.items():
            sss += k * v
        return sss

# https://leetcode.com/problems/sort-characters-by-frequency/submissions/