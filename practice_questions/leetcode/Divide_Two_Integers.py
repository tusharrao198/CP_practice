import math
from typing import List

# https://leetcode.com/problems/divide-two-integers/submissions/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isnegative = (dividend < 0) ^ (divisor < 0)
        # print(isnegative)
        divisor = abs(divisor)
        dividend = abs(dividend)
        remainder = 0
        quotient = 0
        while (dividend - divisor) >= 0:
            sub_quotient = 0
            while (dividend - (divisor << 1 << sub_quotient)) >= 0:
                sub_quotient += 1
            quotient += 1 << sub_quotient
            dividend -= divisor << sub_quotient
            # print("sub_quotient ", sub_quotient)
            # print(
            #     f"quotient = {quotient} and dividend = {dividend} and divisor << 1 << sub_quotient = {divisor << 1 << sub_quotient}"
            # )
        if isnegative:
            return min(max(-(2 ** 31), int(f"-{quotient}")), 2 ** 31 - 1)
        return min(max(-(2 ** 31), quotient), 2 ** 31 - 1)


s = Solution()
x = s.divide(116, 3)

print(x)
