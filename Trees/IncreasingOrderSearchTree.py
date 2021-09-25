# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inordertraversal(self, root, arr):
        if root is None:
            return
        self.inordertraversal(root.left, arr)
        arr.append(root.val)
        self.inordertraversal(root.right, arr)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []  # sorted array from tree
        self.inordertraversal(root, arr)
        # print(arr)

        new_root = TreeNode(arr[0])
        head = new_root

        for i in range(1, len(arr)):
            new_root.right = TreeNode(arr[i])
            new_root = new_root.right

        return head
