# Definition for a binary tree node.
# https://leetcode.com/problems/binary-tree-coloring-game/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root):
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def findx(root, x):
            nonlocal leftnodes, rightnodes
            if root is None:
                return
            if root.val == x:
                leftnodes = self.countNodes(root.left)
                rightnodes = self.countNodes(root.right)
                return
            findx(root.left, x)
            findx(root.right, x)

        leftnodes = rightnodes = parentnodes = 0
        findx(root, x)
        parentnodes = n - (leftnodes + rightnodes + 1)
        print(parentnodes, leftnodes, rightnodes)
        return max(leftnodes, parentnodes, rightnodes) > n / 2
