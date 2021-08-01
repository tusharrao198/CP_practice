from typing import *

# https: // leetcode.com/problems/number-of-1-bits/submissions/

class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = [0]
        # for i in range(1, n+1):
        #     ans.append(sum([int(j) for j in str(bin(i))[2:]]))
        # return ans

        dp = [0]*(n+1)  # dp
        offset = 1
        for i in range(1, n+1):
            if i >= offset*2:
                offset *= 2
            dp[i] = 1+dp[i-offset]
        return dp
