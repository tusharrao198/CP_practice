# https://www.interviewbit.com/problems/intersection-of-sorted-arrays/


class Solution:
    def intersect(self, A, B):
        i = 0
        j = 0
        lst = []
        a = len(A)
        b = len(B)
        while i < a and j < b:
            if A[i] > B[j]:
                j+=1
            elif A[i] < B[j]:
                i+=1
            else:
                lst.append(A[i])
                i+=1
                j+=1
        return lst

s = Solution()

A = [1, 2, 3, 3, 4, 5, 6]
B = [3 ,3, 5]
print(s.intersect(A, B))
