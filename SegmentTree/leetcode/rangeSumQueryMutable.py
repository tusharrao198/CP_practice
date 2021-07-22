from math import ceil, log2
from typing import List


# https://leetcode.com/problems/range-sum-query-mutable/submissions/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = self.buildTree()

    def buildTree(self):
        n = len(self.nums)

        def buildTreeMain(low, high, pos):
            if low == high:
                self.tree[pos] = self.nums[low]
                return self.nums[low]
            mid = (low + high) // 2
            self.tree[pos] = buildTreeMain(low, mid, (2 * pos + 1)) + buildTreeMain(mid + 1, high, (2 * pos + 2))
            return self.tree[pos]

        height = int(ceil(log2(n)))
        max_size = 2 * int(2 ** height) - 1
        self.tree = [0] * max_size
        buildTreeMain(0, n - 1, 0)
        return self.tree

    def update(self, index: int, val: int) -> None:
        n = len(self.nums)

        def updateValMain(low, high, index, diff, pos):
            if index < low or index > high:
                return
            self.tree[pos] += diff

            if low != high:
                mid = (low + high) // 2
                updateValMain(low, mid, index, diff, 2 * pos + 1)
                updateValMain(mid + 1, high, index, diff, 2 * pos + 2)

        if index < 0 or index > n - 1:
            return None
        diff = val - self.nums[index]
        self.nums[index] = val
        updateValMain(0, n - 1, index, diff, 0)
        return

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.nums)

        def rangeSumMain(low, high, qs, qe, pos):
            if qs <= low and qe >= high:
                return self.tree[pos]
            if high < qs or low > qe:
                return 0
            mid = (low + high) // 2
            return rangeSumMain(low, mid, qs, qe, 2 * pos + 1) + rangeSumMain(mid + 1, high, qs, qe, 2 * pos + 2)

        if left < 0 or right > n - 1 or left > right:
            return
        return rangeSumMain(0, n - 1, left, right, 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
