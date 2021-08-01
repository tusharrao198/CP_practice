# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        count_zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
            if nums[i] == 0:
                count_zeros += 1
        j = 0 - count_zeros
        while j < 0:
            nums[j] = 0
            j += 1
        return nums
