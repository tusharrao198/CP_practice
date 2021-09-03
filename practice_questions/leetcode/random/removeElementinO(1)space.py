# https://leetcode.com/problems/remove-element/submissions/
# https://leetcode.com/problems/remove-element


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


