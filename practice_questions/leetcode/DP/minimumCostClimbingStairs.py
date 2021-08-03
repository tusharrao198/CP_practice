# https://leetcode.com/problems/min-cost-climbing-stairs/submissions/
from typing import List

class Solution:
    # Bottom Up Approach
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])

        return min(dp[n-1], dp[n-2])
