from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        
        arr = sorted(nums)
        
        # greater elements put at odd places
        for i in range(1, n, 2):
            nums[i] = arr.pop()
        
        # filling even places with left elements
        for i in range(0, n, 2):
            nums[i] = arr.pop()
            
        return nums

def wiggleSort(nums):
    nums.sort()
    half = len(nums[::2]) - 1
    nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


arr = [8,2,3,4,5,9,6]
arr.sort()
print(arr)
print(arr[::2])
print(arr[1::2])
# print(wiggleSort(arr))
