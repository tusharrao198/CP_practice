# https://www.interviewbit.com/problems/subset/
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A, ans, cur, index):
        if index > len(A):
            return
        ans.append(cur[:])
        for i in range(index, len(A)):
            if A[i] not in cur:
                cur.append(A[i])
                self.solve(A, ans, cur, i)
                x = cur.pop()
        return

    def subsets(self, A):
        ans = []
        cur = []
        A.sort()
        self.solve(A, ans, cur, 0)
        return ans
