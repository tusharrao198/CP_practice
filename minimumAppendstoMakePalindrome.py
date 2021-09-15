# https: // www.interviewbit.com/problems/minimum-appends-for-palindrome/

class Solution:
    # @param A : string
    # @return an integer

    def computeLPS(self, lps, m, ss):
        l = 0  # size
        i = 1

        while(i < m):
            if ss[i] == ss[l]:
                l += 1
                lps[i] = l
                i += 1

            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1

    def solve(self, A):
        ss = A[::-1] + "$" + A
        m = len(ss)
        lps = [0] * m
        self.computeLPS(lps, m, ss)

        return len(A) - lps[-1]
