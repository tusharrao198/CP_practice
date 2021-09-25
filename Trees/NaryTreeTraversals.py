# https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:

    # Post order - Traversal
    def postorder_traversal(self, node, arr):
        if node is None:
            return
        if node.children is not None:
            for child in node.children:
                self.postorder_traversal(child, arr)
            arr.append(node.val)

    def postorder(self, root: "Node") -> List[int]:
        arr = []
        self.postorder_traversal(root, arr)
        return arr

    # preorder - Traversal
    def preorder_traversal(self, node, arr):
        if node is None:
            return
        if node.children is not None:
            arr.append(node.val)
            for child in node.children:
                self.preorder_traversal(child, arr)

    def preorder(self, root: "Node") -> List[int]:
        arr = []
        self.preorder_traversal(root, arr)
        return arr
