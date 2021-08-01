# https://leetcode.com/problems/power-of-two/submissions/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while True:
            if n == 1:
                return True
            elif n % 2 == 0 and n != 0:
                n //= 2
            else:
                break
        return False


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while True:
            if n == 1:
                return True
            elif n % 3 == 0 and n != 0:
                n //= 3
            else:
                break
        return False


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while True:
            if n == 1:
                return True
            elif n % 4 == 0 and n != 0:
                n //= 4
            else:
                break
        return False
