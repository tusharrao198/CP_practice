class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        pos = -1

        if lh<ln:
            return -1
        if lh == 0 and ln == 0:
            return 0
        if lh != 0 and ln == 0:
            return 0
        
        for i in range(lh): 
            if needle in haystack[i:i+ln]:
                return haystack.index(haystack[i:i+ln])        
        return pos