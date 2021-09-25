# https://leetcode.com/problems/leaf-similar-trees/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inordertraversal(self, root, leaf):
        if root is None:
            return
        self.inordertraversal(root.left, leaf)
        if root.left is None and root.right is None:
            leaf.append(root.val)
        self.inordertraversal(root.right, leaf)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        self.inordertraversal(root1, leaf1)
        self.inordertraversal(root2, leaf2)

        n1 = len(leaf1)
        n2 = len(leaf2)
        if n1 != n2:
            return False

        for i in range(n1):
            if leaf1[i] != leaf2[i]:
                return False
        return True
