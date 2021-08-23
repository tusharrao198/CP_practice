# 1647. Minimum Deletions to Make Character Frequencies Unique

# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        dd = collections.Counter(s)
        ans = 0
        used = set()

        for _str, freq in dd.items():

            while freq > 0 and freq in used:
                freq -= 1
                ans += 1

            used.add(freq)

        return ans
