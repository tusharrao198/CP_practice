# https: // leetcode.com/problems/divisor-game/submissions/

class Solution:
    def divisorGame(self, n: int) -> bool:
        # if even ALice will always win
        if n % 2 == 0:
            return True
        return False
