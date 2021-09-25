from typing import List
from bisect import bisect_left, bisect_right

# approach 
# This question uses two concepts maximum suffix array  to retrieve the max element in the right most part of the array 
# which is greater than current element for eg. Array = [2, 5, 3, 6,1, 4, 1]
# maximum suffix array of this would be  = [6, 6, 6, 6, 4, 4, 1]  and then maximum would be present at j+1 th position 
# given that A[j] is the current element

# and self balancing BST for retrieving the maximum element in the 
# left side of the array which is less than the current element in O(logn) time, That is   max(array[:j]) < A[j] , where A[j] is current element

# https: // www.geeksforgeeks.org/largest-element-smaller-than-current-element-on-left-for-every-element-in-array/
# https: // www.interviewbit.com/problems/maximum-sum-triplet/
# https://docs.python.org/3/library/bisect.html
# https: // www.youtube.com/watch?v = l_hPdol4CSU

class Solution:
    # @param A : list of integers
    # @return an integer

    def find_lt(self, a, x):
        # 'Find rightmost value less than x'
        i = bisect_left(a, x)
        if i:
            return i-1
        return -1

    def solve(self, A):
        n = len(A)
        overall_max_ans=0
        max_sum_val = A[-1] # maximum sum in max_suffix_array
        max_suffix_arr = [-1]*n

        max_suffix_arr[-1] = A[-1]
        for i in reversed(range(n-1)):
            max_sum_val = max(max_sum_val, A[i])
            max_suffix_arr[i] = max_sum_val


        print(f"max = {max_suffix_arr}")
        # max_suffix_array for (j+1)th to n elements     
        track = []
        track.append(A[0])
        for j in range(1, n-1):            
            res = self.find_lt(track, A[j])
            if (res!=-1):
                if max_suffix_arr[j+1] <= A[j]:
                    continue
                overall_max_ans = max(
                    overall_max_ans, max_suffix_arr[j+1] + A[j] + track[res])
            # print(f"overall_max_ans = {overall_max_ans}")
            track.insert(res+1, A[j])
        return overall_max_ans


s = Solution()
# arr = [-1, 0, 1, 2, -1, -4]
arr = [2, 5, 3, 6,1, 4, 1]
# arr = [18468, 6335, 26501, 19170, 15725, 11479, 29359, 26963, 24465, 5706,
    #    28146, 23282, 16828, 9962, 492, 2996, 11943, 4828, 5437, 32392, 14605]

# arr = [3, 0, -2, -1, 1, 2]
x = s.solve(arr)
print(x)

# ------------------ this is TLE case but approach was right using backtracking ----------------------
# class Solution:
#     def maxSumTriplet(self, nums, cur, max_, index):
#         if len(cur) == 3:
#             max_[0] = max(max_[0], sum(cur))
#         else:
#             for i in range(index, len(nums)):
#                 if len(cur) < 3:
#                     if len(cur) == 0:
#                         cur.append(nums[i])
#                         self.maxSumTriplet(nums, cur, max_, i + 1)
#                         cur.pop()

#                     elif len(cur) >= 1 and nums[i] > cur[-1]:
#                         cur.append(nums[i])
#                         self.maxSumTriplet(nums, cur, max_, i + 1)
#                         cur.pop()
#         return


#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         max_ = [float("-inf")]
#         cur = []
#         self.maxSumTriplet(nums, cur, max_, index=0)
#         return max_[0]


# ------------------ working solution below---------------------
# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         n = len(A)
#         right_max = [-1] * n
#         maxi = A[-1]

#         for i in reversed(range(n - 1)):
#             print(f"A[i] = {A[i]}")
#             right_max[i] = maxi
#             maxi = max(maxi, A[i])
#         print(f"right_max = {right_max}")
#         print(f"maxi = {maxi}")
#         sk = []
#         c = 0
#         for i in range(n):
#             print(f"sk = {sk} and i = {i} and  A[i] = {A[i]} and max = {c}")
#             if sk:
#                 while sk and sk[-1] >= right_max[i]:
#                     sk.pop()
#                 while sk and sk[-1] < A[i] and A[i] < right_max[i]:
#                     c = max(c, sk[-1] + A[i] + right_max[i])
#                     sk.pop()
#             sk.append(A[i])
#         return c
