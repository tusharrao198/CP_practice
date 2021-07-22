# Definition for a binary tree node.

# https: // leetcode.com/problems/path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root,  target, cur):
        if root is not None:
            # print("node -> ", root.val)
            cur+=root.val
            if cur==target and root.right is None and root.left is None:
                return True
            return self.solve(root.right, target, cur) or self.solve(root.left, target, cur)
        return False

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        cur = 0
        return self.solve(root, targetSum, cur)
