class Solution:
    def firstMissingPositive(self, A):
        n = len(A)
        for i in range(n):
            if A[i] <= 0 or A[i] > n:
                A[i] = n + 1

        for i in range(n):
            if abs(A[i]) <= n:
                A[abs(A[i]) - 1] = -abs(A[abs(A[i]) - 1])

        for i in range(n):
            if A[i] > 0:
                return i + 1

        return n + 1


# https: // www.interviewbit.com/problems/first-missing-integer/

# https://leetcode.com/problems/first-missing-positive/submissions/