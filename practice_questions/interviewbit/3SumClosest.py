# https://www.interviewbit.com/problems/3-sum/


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        closest = None
        for i in range(len(A) - 2):
            j, k = i + 1, len(A) - 1
            while k > j:
                threeSum = A[i] + A[j] + A[k]
                if threeSum == B:
                    return threeSum
                if closest is None or abs(B - threeSum) < abs(B - closest):
                    closest = threeSum
                if threeSum < B:
                    j += 1
                else:
                    k -= 1
        return closest
