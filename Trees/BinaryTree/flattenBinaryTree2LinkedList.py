# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        def solve(root):
            if not root:
                return
            temp = root.right
            solve(root.left)
            root.right = root.left
            curr = root
            while curr.right:
                curr = curr.right
            curr.right = temp
            solve(temp)
            root.left = None

        solve(A)
        return A
