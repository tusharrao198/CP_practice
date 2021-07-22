# https: // leetcode.com/problems/search-in-a-binary-search-tree/submissions/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # print(f"search current Node is -> {node.data}")
        if root is None:
            # print("Not Found")
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)
