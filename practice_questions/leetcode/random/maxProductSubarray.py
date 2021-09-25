from typing import List
# https://www.youtube.com/watch?v=hJ_Uy2DzE08

# https://leetcode.com/problems/maximum-product-subarray/submissions/


class Solution:
    # O(n) complexity ans O(1) space
    def maxProduct(self, nums: List[int]) -> int:
        ans, cur_max, cur_min = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp = cur_max
            cur_max = max(nums[i], cur_max * nums[i], cur_min * nums[i])
            cur_min = min(nums[i], temp * nums[i], cur_min * nums[i])
            ans = max(ans, cur_max)
        return ans


# O(n^2) TC  and O(n) space
#     def solve(self, anslist, nums, curmax, index):
#         while index >= 0:
#             if len(curmax) == 0:
#                 curmax.append(nums[index])
#             else:
#                 curmax.append(curmax[-1] * nums[index])
#             if index == 0:
#                 x = max(max(anslist), max(curmax))
#                 if x not in anslist:
#                     anslist.append(x)
#             index -= 1
#         return

#     def maxProduct(self, nums: List[int]) -> int:
#         anslist = [nums[0], nums[-1]]
#         curmax = []
#         for i in range(1, len(nums)):
#             self.solve(anslist, nums, curmax, index=i)
#             curmax = []
#         return max(anslist)

s = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr1 = [-1]
arr2 = [-2, 0, -1]
arr3 = [-3, -1, -2]
arr4 = [3, -1, 4]
arr5 = [2, -5, -2, -4, 3]
l = [arr, arr1, arr2, arr3, arr4, arr5]
for arr in l:
    ans = s.maxProduct(arr)
    print(ans, "\n")

# arr5 = [2, 3, -2, 4]
# ans = s.maxProduct(arr5)
# print(ans, "\n")
