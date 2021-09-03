class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A == B:
            return A
        if A == 0:
            return B
        if B == 0:
            return A
        if A > B:
            return self.gcd(B, A % B)
        else:
            return self.gcd(A, B % A)
