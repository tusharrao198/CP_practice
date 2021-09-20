class Solution:
    def solve(self, A):
        dd = {}
        for i in A:
            dd[i] = dd.get(i, 0) + 1
        ce, co = 0, 0
        for i in dd.values():
            if i%2==0: ce +=i
            else:
                if co>1:
                    return 0
                co+=i 
        x = len(A)
        if x%2==0 and ce==x: return 1
        if x%2!=0 and co%2!=0 and ce%2==0 and ce+co==x: return 1
        return 0
        
# https://www.interviewbit.com/problems/check-palindrome/
