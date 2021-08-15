# https://leetcode.com/problems/count-sorted-vowel-strings/


class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1] * 5
        ans = 0
        while ans < n - 1:
            for i in range(5):
                arr[i] = sum(arr[i:])
            ans += 1
        return sum(arr)
