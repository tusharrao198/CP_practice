# https://www.interviewbit.com/problems/vowel-and-consonant-substrings/

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vow = ['a', 'e', 'i', 'o', 'u']
        mod = 10**9 + 7
        n = len(A)
        vc = 0  # vowels count in string
        for i in vow:
            vc += A.count(i)
        ans = (vc * (n-vc)) % mod
        return ans
