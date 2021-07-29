from typing import List

# in O(1) space and O(n) time
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        return


#----------------------------------------------------------------------
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()  # sort array in O(nlogn) time
        for i in range(1, len(nums)):  # traverse in O(n)
            if nums[i] == nums[i-1]:
                return nums[i]

# Total time = O(nlogn) and O(n) space

#--------------------------------------------------
# in O(n) space and time O(n) using hashing
def findDuplicate(A):
        dd = {}
        for i in A:
            dd[i] = dd.get(i, 0) + 1
        n = len(A)
        for k, v in dd.items():
            if v > 1:
                return k
        return -1





