from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums.replace(nums[i], False)
        print(nums)
        count = 0
        for i in nums:
            if i:
                count += 1
        return count


s = Solution()
arr = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
x = s.removeElement(arr, val)
print(x)
