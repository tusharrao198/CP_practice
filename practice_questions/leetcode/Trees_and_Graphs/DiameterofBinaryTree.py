# Definition for a binary tree node.

# https: // leetcode.com/problems/diameter-of-binary-tree/submissions/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = float("-inf")

    def solve(self, root):
        if root is None or root.val is None:
            return 0

        l = self.solve(root.left)
        r = self.solve(root.right)

        temp_ans = max(l, r) + 1
        ans = max(temp_ans, 1+l+r)
        self.res = max(self.res, ans)

        return temp_ans

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return self.res - 1
