class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        c = "".join(A)

        import string
        alp = list(string.ascii_lowercase)
        alp1 = list(string.ascii_uppercase)
        alp.extend(alp1)
        alp = set(alp)
        
        for i in c:
            if i in alp:
                continue
            else:
                return 0
        return 1
                
            
            
