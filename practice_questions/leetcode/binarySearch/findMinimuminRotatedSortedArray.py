# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid + 1

        if nums[0] > nums[l]:
            return nums[l]
        return nums[0]

    def findMin1(self, arr):
        n = len(arr)
        l, r = 0, n - 1

        while l <= r:
            mid = l + (r - l) // 2
            nex = (mid + 1) % n
            prev = (mid + n - 1) % n

            # print(mid, arr[mid], prev, nex, l, r)

            if arr[prev] >= arr[mid] and arr[mid] <= arr[nex]:
                return mid

            if arr[n - 1] <= arr[mid]:
                l = mid + 1

            elif arr[mid] <= arr[n - 1]:
                r = mid - 1
        # return mid


arr = [4, 5, 6, 7, 0, 1, 2]
s = Solution()

print(s.findMin1(arr))
