# https://leetcode.com/problems/palindrome-partitioning/submissions/

from typing import List

# backtracking


class Solution:
    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def findPalindromes(self, s, ans, cur, index):
        if index == len(s):
            ans.append(cur[:])
            return

        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                cur.append(s[index : i + 1])
                self.findPalindromes(s, ans, cur, i + 1)
                cur.pop()
        return

    def partition(self, s: str) -> List[List[str]]:
        ans, cur = [], []
        self.findPalindromes(s, ans, cur, index=0)
        return ans
