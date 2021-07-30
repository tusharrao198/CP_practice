from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate
import sys
from math import ceil, log2

MAX_SIZE = sys.maxsize
MIN_SIZE = float("-inf")


class RangeMin:
    def getMid(self, a, b):
        return (a + b) // 2


    def buildTreeMain(self, tree, arr, low, high, pos):
        if low == high:
            tree[pos] = arr[low]
            # print(arr[low])
            return arr[low]
        mid = self.getMid(low, high)
        tree[pos] = min(self.buildTreeMain(tree, arr, low, mid, (2 * pos + 1)),
                        self.buildTreeMain(tree, arr, mid + 1, high, 2 * pos + 2))

        return tree[pos]

    def buildTree(self, arr, n):
        height = int(ceil(log2(n)))
        max_size = 2 * int(2 ** height) - 1
        tree = [0] * max_size
        self.buildTreeMain(tree, arr, 0, n - 1, 0)
        return tree

    def updateValMain(self, tree, low, high, index, new_val, pos):
        if low == high:
            tree[pos] = new_val
        else:
            mid = self.getMid(low, high)
            if low <= index <= mid:
                self.updateValMain(tree, low, mid, index, new_val, 2*pos+1)
            else:
                self.updateValMain(tree, mid + 1, high, index, new_val, 2 * pos + 2)
            tree[pos] = min(tree[2*pos+1], tree[2*pos+2])
        return

    def updateVal(self, tree, arr, n, index, new_val):
        if index < 0 or index > n - 1:
            return "INVALID INDEX"
        arr[index] = new_val
        self.updateValMain(tree, 0, n - 1, index, new_val, 0)

    def rangeMinMain(self, tree, low, high, qs, qe, pos):
        if qs <= low and qe >= high:
            return tree[pos]
        # If segment of this node
        # is outside the given range
        if high < qs or low > qe:
            return MAX_SIZE
        # If a part of this segment
        # overlaps with the given range
        mid = self.getMid(low, high)
        return min(self.rangeMinMain(tree, low, mid, qs, qe, 2 * pos + 1),
                self.rangeMinMain(tree, mid + 1, high, qs, qe, 2 * pos + 2))

    def rangeMin(self, tree, n, qs, qe):
        if qs < 0 or qe > n - 1 or qs > qe:
            return "INVALID INPUT"
        return self.rangeMinMain(tree, 0, n - 1, qs, qe, 0)


class RangeMax:
    def getMid(self, a, b):
        return (a + b) // 2

    def buildTreeMain(self, tree, arr, low, high, pos):
        if low == high:
            tree[pos] = arr[low]
            # print(arr[low])
            return arr[low]
        mid = self.getMid(low, high)
        tree[pos] = max(self.buildTreeMain(tree, arr, low, mid, (2 * pos + 1)),
                        self.buildTreeMain(tree, arr, mid + 1, high, 2 * pos + 2))

        return tree[pos]

    def buildTree(self, arr, n):
        height = int(ceil(log2(n)))
        max_size = 2 * int(2 ** height) - 1
        tree = [0] * max_size
        self.buildTreeMain(tree, arr, 0, n - 1, 0)
        return tree

    def updateValMain(self, tree, low, high, index, new_val, pos):
        if low == high:
            tree[pos] = new_val
        else:
            mid = self.getMid(low, high)
            if low <= index <= mid:
                self.updateValMain(tree, low, mid, index, new_val, 2*pos+1)
            else:
                self.updateValMain(tree, mid + 1, high,
                                   index, new_val, 2 * pos + 2)
            tree[pos] = max(tree[2*pos+1], tree[2*pos+2])
        return

    def updateVal(self, tree, arr, n, index, new_val):
        if index < 0 or index > n - 1:
            return "INVALID INDEX"
        arr[index] = new_val
        self.updateValMain(tree, 0, n - 1, index, new_val, 0)

    def rangeMaxMain(self, tree, low, high, qs, qe, pos):
        if qs <= low and qe >= high:
            return tree[pos]
        # If segment of this node
        # is outside the given range
        if high < qs or low > qe:
            return MIN_SIZE
        # If a part of this segment
        # overlaps with the given range
        mid = self.getMid(low, high)
        return max(self.rangeMaxMain(tree, low, mid, qs, qe, 2 * pos + 1),
                   self.rangeMaxMain(tree, mid + 1, high, qs, qe, 2 * pos + 2))

    def rangeMax(self, tree, n, qs, qe):
        if qs < 0 or qe > n - 1 or qs > qe:
            return "INVALID INPUT"
        return self.rangeMaxMain(tree, 0, n - 1, qs, qe, 0)


tt = int(input())
for _ in range(tt):
    n = int(input())
    arr = list(map(int, input().split()))
    min_ = RangeMin()
    max_ = RangeMax()
    segment_tree_min = min_.buildTree(arr, n)
    segment_tree_max = max_.buildTree(arr, n)
    prod_max = float("-inf")

    for i in range(n):
        for j in range(i+1, n):
            mn = min_.rangeMin(segment_tree_min, n, i, j)
            mx = max_.rangeMax(segment_tree_max, n, i, j)
            prod_max = max(prod_max, mn*mx)

    print(prod_max)


