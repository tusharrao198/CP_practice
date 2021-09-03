class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x > 0:
            ans = int("".join(list(str(x))[::-1]))
        elif x == 0:
            ans = 0
        else:
            b = "-"
            b += "".join(list(str(x)[1:])[::-1])
            ans = int(b)

        if ans in range(-2**31, 2**31):
            return ans
        return 0

S = Solution()
ans = S.reverse(-1)
print(ans)