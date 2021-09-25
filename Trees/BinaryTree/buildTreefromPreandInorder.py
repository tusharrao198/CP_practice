# https://www.interviewbit.com/problems/construct-binary-tree-from-inorder-and-preorder/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param preorder : list of integers
    # @param inorder : list of integers
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None

        root_pos = inorder.index(preorder[0])
        new_node = TreeNode(preorder[0])

        new_node.left = self.buildTree(preorder[1 : root_pos + 1], inorder[:root_pos])

        new_node.right = self.buildTree(
            preorder[root_pos + 1 :], inorder[root_pos + 1 :]
        )

        return new_node


#########################################################################################

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
    return -1


def buildTree(preorder, inorder, start, end):
    if start > end:
        return None

    curr = Node(preorder[buildTree.idx])
    buildTree.idx += 1

    if start == end:
        return curr

    # pos = search(inorder, start, end, curr.val)
    pos = dd[curr.val]
    curr.left = buildTree(preorder, inorder, start, pos - 1)
    curr.right = buildTree(preorder, inorder, pos + 1, end)

    return curr


# left => root => right
def inOrderTraversal(node):
    if node is not None:
        inOrderTraversal(node.left)
        print(node.val, end=" ")
        inOrderTraversal(node.right)


preorder = [1, 2, 4, 3, 5]
inorder = [4, 2, 1, 5, 3]
dd = {v: k for k, v in enumerate(inorder)}

# static variable
buildTree.idx = 0

n = len(inorder)
root = buildTree(preorder, inorder, 0, n - 1)
inOrderTraversal(root)
