from typing import *


# with O(n) space complexity
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        ans = []
        while (i < m and nums1[i]) and (j < n and nums2[j]):
            if nums1[i] > nums2[j]:
                ans.append(nums2[j])
                j += 1
            else:
                ans.append(nums1[i])
                i += 1

        while i < m and nums1[i] is not None:
            ans.append(nums1[i])
            i += 1

        while j < n and nums2[j] is not None:
            ans.append(nums2[j])
            j += 1

        return ans


# without O(n) space complexity  not completed yet

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        ans = []
        while (i < m and nums1[i] is not None) and (j < n and nums2[j] is not None):
            print(
                f"start i = {i} j = {j} and nums1[i] > nums2[j] = {nums1[i] , nums2[j]}"
            )
            if nums1[i] > nums2[j]:
                nums1[i] = nums2[j]
                # ans.append(nums2[j])
                j += 1

            i += 1
        print(i, j)
        while i < m and nums1[i] is not None:
            # ans.append(nums1[i])
            i += 1

        print(f"b = > {i, j}")
        while j < n and nums2[j] is not None:
            nums1[i] = nums2[j]
            j += 1
            i += 1
        print(f"C = > {i, j}")
        return nums1


s = Solution()
arr1 = [1, 2, 3, 0, 0, 0]
m = 3
arr2 = [2, 5, 6]
n = 3

ans = s.merge(arr1, m, arr2, n)
print(ans)
