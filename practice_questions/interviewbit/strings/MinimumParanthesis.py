# https://www.interviewbit.com/problems/minimum-parantheses/
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        _open = 0
        _close = 0
        for i in A:
            if i == "(":
                _open += 1
            elif i == ")":
                if _open > 0:
                    _open -= 1
                else:
                    _close += 1
        return abs(_open+_close)
