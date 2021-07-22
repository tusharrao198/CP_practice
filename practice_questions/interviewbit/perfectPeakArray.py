# Solution Approach
# An Efficient Solution can solve this problem in O(N) time using O(N) extra space. Below is detailed solution.

# Create two arrays leftMax[] and rightMin[].
# Traverse input array from left to right and fill leftMax[] such that leftMax[i] contains maximum element from 0 to i-1 in input array.
# Traverse input array from right to left and fill rightMin[] such that rightMin[i] contains minimum element from to N-1 to i+1 in input array.
# Traverse input array. For every element A[i], check if A[i] is greater than leftMax[i] and smaller than rightMin[i]. If yes, return 1.
# If loops exits and no such element found return 0
# A Further Optimization to the above approach is to use only one extra array and traverse input array only twice.
# The first traversal is the same as above and fills leftMax[]. Next traversal traverses from the right and keeps track of the minimum. The second traversal also finds the required element.

# Time Complexity: O(N)
# Auxiliary Space: O(N)


# https://www.interviewbit.com/problems/perfect-peak-of-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        rightmin = [A[-1]]*len(A)
        min_ = A[-1]
        for i in reversed(range(len(A)-1)):
            min_ = min(min_, A[i])
            rightmin[i] = min_
        # print(rightmin)

        leftMax = [A[0]]*len(A)
        max_ = A[0]
        for i in range(1, len(A)):
            max_ = max(max_, A[i])
            leftMax[i] = max_
        # print(leftMax)

        for i in range(1, len(A)-1):
            if A[i]>leftMax[i-1] and A[i]<rightmin[i+1]:
                return 1
        return 0
    

S = Solution()
A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
x = S.perfectPeak(A)

print(x)
