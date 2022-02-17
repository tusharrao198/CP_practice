from typing import List

class Solution:
    # sol1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):                
                if nums[i]+nums[j]==target:
                    pos.append(i)
                    pos.append(j)
                    break
                else:
                    continue
        return pos
    
    #################
    # sol2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pos.keys():
                return [pos[diff], i]
            pos[nums[i]] = i
        