# https://www.interviewbit.com/problems/binary-tree-from-inorder-and-postorder/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if not A:
            return None

        root_pos = A.index(B[-1])
        new_node = TreeNode(B[-1])

        new_node.left = self.buildTree(A[:root_pos], B[:root_pos])
        new_node.right = self.buildTree(A[root_pos + 1 :], B[root_pos:-1])

        return new_node


# Binary Tree Node
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def search(inorder, start, end, curr):
    for i in range(start, end + 1):
        if inorder[i] == curr:
            return i


def buildTree(postorder, inorder, start, end):
    if start > end:
        return None

    curr = Node(postorder[buildTree.idx])
    buildTree.idx -= 1

    if start == end:
        return curr

    # pos = search(inorder, start, end, curr.val)
    pos = dd[curr.val]
    curr.right = buildTree(postorder, inorder, pos + 1, end)
    curr.left = buildTree(postorder, inorder, start, pos - 1)

    return curr


# left => root => right
def inOrderTraversal(node):
    if node is not None:
        inOrderTraversal(node.left)
        print(node.val, end=" ")
        inOrderTraversal(node.right)


postorder = [4, 2, 5, 3, 1]
inorder = [4, 2, 1, 5, 3]
dd = {v: k for k, v in enumerate(inorder)}
n = len(inorder)

# static variable
buildTree.idx = n - 1

root = buildTree(postorder, inorder, 0, n - 1)
inOrderTraversal(root)
