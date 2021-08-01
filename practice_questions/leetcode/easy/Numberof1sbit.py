# https://leetcode.com/problems/number-of-1-bits/submissions/

class Solution:
    # approach using AND operator 1&0 = 0 and 1&1 = 1
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            print(n&1)
            if n&1==1: 
                count +=1
            n>>=1
        return count

