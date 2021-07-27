class Solution:
    def isMonotonic(self, n, x):
        for i in range(1, x):
            if int(n[i]) < int(n[i-1]):
                return False
        return True
        
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = list(str(n))
        x = len(n)        
        if not self.isMonotonic(n, x):
            i = 0
            for j in range(1, x):
                if  int(n[j]) < int(n[j-1]):
                    i = j -1
                    break

            while i>0 and int(n[i-1]) > int(n[i]) -1:
                i-=1

            n[i] = str(int(n[i]) - 1)

            for j  in range(i + 1, x):
                n[j] = '9'

        return int("".join(n))
                
            
# https://leetcode.com/problems/monotone-increasing-digits/submissions/

