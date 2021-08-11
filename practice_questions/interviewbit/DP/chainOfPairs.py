# https: // www.interviewbit.com/problems/chain-of-pairs/


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        lst = [1] * n

        for i in range(1, n):
            for j in range(i):
                if A[i][1] > A[j][1] and A[i][0] > A[j][1] and lst[i] < lst[j]+1:
                    lst[i] = lst[j] + 1
        ans = max(lst)
        return ans
