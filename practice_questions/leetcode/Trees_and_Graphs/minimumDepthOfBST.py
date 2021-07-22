# Definition for a binary tree node.
# https: // leetcode.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def minDepth(self, root: TreeNode) -> int:
    # TC :- O(n)  and SC:- O(h) h=> height of tree

        if root is None:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if root.left is None or root.right is None:  
            return 1 + max(left, right)
            
        return min(left, right) + 1
