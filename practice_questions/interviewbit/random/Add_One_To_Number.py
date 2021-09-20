import math
class Solution:

    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        i = len(A)-1
        ans = 1
        while i < len(A) and i >= 0:
            ans += A[i]
            carry = math.floor(ans/10)
            if carry == 0:
                A[i] = ans
                break
            elif carry == 1:
                A[i] = ans % 10
                ans = carry
            i -= 1
        A = [carry] + A
        while A[0] == 0:
            del A[0]
        return A



# second solution
# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def plusOne(self, A):
#         A = [str(_) for _ in A]
#         A = str(int("".join(A)) + 1)
#         return list(A)

s = Solution()
arr =  [1,2,3]
arr = [0]
x = s.plusOne(arr)
print(x)
