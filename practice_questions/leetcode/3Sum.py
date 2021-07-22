from typing import List

# https://leetcode.com/problems/3sum/submissions/
# https://leetcode.com/problems/3sum
# https://www.geeksforgeeks.org/count-pairs-with-given-sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, track = [], set()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            current = nums[i]
            while l < r:
                target = current + nums[l] + nums[r]
                if target == 0:
                    if str([current, nums[l], nums[r]]) not in track:
                        ans.append([current, nums[l], nums[r]])
                        track.add(str([current, nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
        return ans


s = Solution()
arr = [-1, 0, 1, 2, -1, -4]
# arr = [3, 0, -2, -1, 1, 2]
x = s.threeSum(arr)
print(x)

# below approach works but TLE in both

# class Solution:
    # def solve(self, nums, ans, cur, index):
    #     if len(cur) == 3 and sum(cur) == 0:
    #         ans.append(cur[:])
    #         ans.add()
    #     else:
    #         for i in range(index, len(nums)):
    #             # print(f"len(cur) = {len(cur)} and nums[i]= {nums[i]}")
    #             if len(cur) < 3:
    #                 cur.append(nums[i])
    #                 # print(f"cur = {cur} and ans = {ans}")
    #                 self.solve(nums, ans, cur, i + 1)
    #                 # print(f"pop =")
    #                 cur.pop()
    #     return

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     ans, cur = [], []
    #     nums.sort()
    #     self.solve(nums, ans, cur, index=0)
    #     return ans


# from itertools import combinations
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         pairs = list(set(combinations(nums, 3)))
#         n = len(nums)
#         ans = []
#         for i in range(len(pairs)):
#             if (sum(pairs[i])==0):
#                 ans.append(pairs[i])
#         return ans
