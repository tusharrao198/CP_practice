# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inordertraversal(self, root, arr):
        if root is None:
            return
        self.inordertraversal(root.left, arr)
        arr.append(root.val)
        self.inordertraversal(root.right, arr)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []  # sorted array from tree
        self.inordertraversal(root, arr)
        # print(arr)
        _sum = 0
        for i in range(len(arr)):
            if low <= arr[i] <= high and arr[i] is not None:
                _sum += arr[i]
        return _sum
