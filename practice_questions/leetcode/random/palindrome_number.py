class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = "".join(list(str(x)))[::-1]
        if str(x) == a:
            return True
        return False


# https://leetcode.com/problems/palindrome-number/submissions/
