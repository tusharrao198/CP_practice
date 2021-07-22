class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        ans = 1
        while i < len(digits) and i >= 0:
            ans += digits[i]
            carry = math.floor(ans / 10)
            if carry == 0:
                digits[i] = ans
                break
            elif carry == 1:
                digits[i] = ans % 10
                ans = carry
            i -= 1
        digits = [carry] + digits
        while digits[0] == 0:
            del digits[0]
        return digits
