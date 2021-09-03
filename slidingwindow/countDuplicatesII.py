import collections as cc

# arr = [1,2,3,1]
# arr = ['a','b', 'c', 'a']

# print(enumerate(arr))

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # dic = {}
        # for i, v in enumerate(nums):
        #     if v in dic and i - dic[v] <= k:
        #         return True
        #     dic[v] = i
        # return False

        dd = {}
        for i in range(len(nums)):
            if nums[i] in dd and (i - dd[nums[i]]) <= k:
                return True
            dd[nums[i]] = i
        return False

s = Solution()

arr = [1, 2, 3, 1, 2, 3]
k = 2
ans = s.containsNearbyDuplicate(arr, k)
print(ans)


# for index, val in enumerate(arr):
#     print(index, val)
# ss = cc.Counter(arr)

# print(ss)

# for a, b in ss.items():
#     print(a,b)
