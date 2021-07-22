# Definition for a binary tree node.
from typing import List
# https: // leetcode.com/problems/binary-tree-postorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root, arr):
        if root is not None:
            self.solve(root.left, arr)
            self.solve(root.right, arr)
            arr.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root is not None:
            self.solve(root, ans)
        return ans
