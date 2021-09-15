# https: // www.interviewbit.com/problems/convert-to-palindrome/

class Solution:
    # @param A : string
    # @return an integer

    def isPalindrome(self, s):
        n = len(s)
        i = 0
        j = n - 1

        while i<=j:
            if s[i]!=s[j]:
                return 0
            else:
                i+=1
                j-=1
        return 1

    def solve(self, A):
        m = len(A)
        i = 0
        j = m - 1
        while i<=j:
            if A[i]!=A[j]:
                if self.isPalindrome(A[i+1:j+1]) or self.isPalindrome(A[i:j]):
                    return 1
                else:
                    return 0
            else:
                i+=1
                j-=1
        return 1

        


