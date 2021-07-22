# Definition for a binary tree node.
# https: // leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # TC :- O(n)  and SC:- O(h) h=> height of tree
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
            
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1



