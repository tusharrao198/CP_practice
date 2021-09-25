# https://leetcode.com/problems/roman-to-integer/submissions/

# https://leetcode.com/problems/roman-to-integer
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        sym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if n == 1:
            return sym[s]
        ans = 0
        i = 0
        while i < n:
            # print(i)
            a = sym[s[i]]
            if i < n - 1:
                b = sym[s[i + 1]]
                if b > a:
                    ans += abs(b - a)
                    i += 1
                else:
                    ans += a
            else:
                ans += a
            i += 1
        return ans


s = Solution()
ss = "MCMXCIV"
x = s.romanToInt(ss)
print(x)
