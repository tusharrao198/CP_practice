# https://www.interviewbit.com/problems/amazing-subarrays/
class Solution:
    def solve(self, A):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', "E", "I", "O", "U"]
        mod = 10003
        n = len(A)
        c = 0 
        for i in range(n):
            if A[i] in vowels:
                c = (c + (n - i)) % mod 
        return c % mod