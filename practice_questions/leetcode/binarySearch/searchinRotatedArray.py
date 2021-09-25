# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
from typing import List

# https://www.youtube.com/watch?v=W3-KgsCVH1U&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=9

# Approach: Find minimum element's index in the given array. On observing , minimum element's left side of array and right side of array are sorted so, now we can apply apply binary search on both of these array and find if target value is present or not.


class Solution:
    def minimumElement(self, arr):
        n = len(arr)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2

            if arr[mid] < arr[0]:
                r = mid
            else:
                l = mid + 1

        if arr[0] > arr[l]:
            return l
        return 0

    def searchMain(self, arr, target):  # simple binary search
        n = len(arr)
        l, r = 0, n - 1

        while l <= r:

            mid = l + (r - l) // 2

            if arr[mid] == target:
                return True, mid

            elif arr[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False, -1

    def search(self, nums: List[int], target: int) -> int:
        minele = self.minimumElement(nums)  # return index of min element

        a = self.searchMain(nums[:minele], target)
        b = self.searchMain(nums[minele:], target)

        if a[0]:
            return a[1]
        if b[0]:
            return minele + b[1]

        return -1


s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(s.search(nums, target))
