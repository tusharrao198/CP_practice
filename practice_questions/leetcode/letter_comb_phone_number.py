# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List
class Solution:
    def solve(self, dd, ans, cur_combination, digits, index):
        if index>len(digits):
            return

        if len(cur_combination) == len(digits):
            ans.append(cur_combination[:])
            return 

        cur_str = dd[int(digits[index])]
        for i in range(len(cur_str)):
            self.solve(dd, ans, cur_combination+cur_str[i], digits,index +1)        

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits) == 0:
            return ans
        alpha = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        dd = {}
        for i in range(2,10):
            dd[i] = alpha[i-2]
        cur_combination = ""
        self.solve(dd, ans, cur_combination, digits, 0)
        return ans

s = Solution()
x = s.letterCombinations('23')
print(x)
