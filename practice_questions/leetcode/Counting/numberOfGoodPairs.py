from typing import List

# https://leetcode.com/problems/number-of-good-pairs/submissions/

class Solution:
    def numIdenticalPairs(nums: List[int]) -> int:
        nums_dict = {}
        sum_pairs = 0

        def fact(number):
            if number > 1:
                return number * fact(number - 1)
            elif number <= 1:
                return 1

        def combination(n):
            if n >= 2:
                combination_cal = fact(n) / (2 * (fact(n - 2)))
                return int(combination_cal)
            else:
                return 0

        for i in range(0, len(nums)):
            nums_dict[nums[i]] = nums_dict.get(nums[i], 0) + 1
        # print(nums_dict)
        for key in nums_dict:
            x = combination(nums_dict[key])
            # print(key, x)
            sum_pairs += x
        return sum_pairs

########################################################################################################

# O(n^2) solution
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#         return count
