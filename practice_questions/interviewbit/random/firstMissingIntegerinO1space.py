# https: // www.interviewbit.com/problems/first-missing-integer/

# https://leetcode.com/problems/first-missing-positive/submissions/

# in O(1) space and O(n) time 
class Solution:
    def firstMissingPositive(self, A):
        n = len(A)
        for i in range(n):
            if A[i] <= 0 or A[i] > n:
                A[i] = n + 1
        print(A)
        for i in range(n):
            if abs(A[i]) <= n:
                A[abs(A[i]) - 1] = -abs(A[abs(A[i]) - 1])
        print(A)
        for i in range(n):
            if A[i] > 0:
                return i + 1
        print(A)
        return n + 1

s = Solution()
ar = [3, 2, 0,-4,-1, 5]
print(ar)
x = s.firstMissingPositive(ar)
print(x)