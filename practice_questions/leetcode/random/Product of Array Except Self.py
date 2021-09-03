from typing import List

# explanation :- https://www.youtube.com/watch?v=gREVHiZjXeQ

# https://leetcode.com/problems/product-of-array-except-self/submissions/

# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [], [1 for _ in range(n)]

        # cumulative left
        for i in range(n):
            if i == 0:
                left.append(nums[i])
            else:
                left.append(left[-1] * nums[i])

        # cumulative right
        prev = -1
        for i in range(n):
            j = n - 1 - i
            if i == 0:
                right[j] = nums[j]
            else:
                right[j] = right[prev] * nums[j]
            prev = j

        ans = []
        for i in range(n):
            if i == 0:
                ans.append(right[i + 1])
            elif i == n - 1:
                ans.append(left[i - 1])
            else:
                ans.append(left[i - 1] * right[i + 1])

        return ans


s = Solution()
arr = [1, 2, 3, 4]
a = s.productExceptSelf(arr)
print(a)
