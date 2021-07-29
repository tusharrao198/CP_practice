# Merge Two Sorted Lists II
# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

class Solution:
    # def merge(self, A, B):
    #     for i in B:
    #         A.append(i)
    #     A.sort()
    #     return A

    def merge(self, A, B):
        i, j = 0, 0
        lst = []
        a, b = len(A), len(B)

        while i < a and j < b:
            if A[i] > B[j]:
                lst.append(B[j])
                j += 1
            elif A[i] < B[j]:
                lst.append(A[i])
                i += 1
            else:
                lst.append(A[i])
                lst.append(B[j])
                i += 1
                j += 1
        while i< a:
            lst.append(A[i])
            i+=1
        
        while j< b:
            lst.append(B[j])
            j+=1
        
        return lst


s = Solution()

A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 3, 5]
print(s.merge(A, B))
