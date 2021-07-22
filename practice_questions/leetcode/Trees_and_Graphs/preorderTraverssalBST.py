# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def solve(self, root, arr):
        if root is not None:
            arr.append(root.val)
            self.solve(root.left, arr)
            self.solve(root.right, arr)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root is not None:
            self.solve(root, ans)
        return ans
