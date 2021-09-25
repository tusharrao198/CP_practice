# Definition for a  binary tree node


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers

    def findpath(self, root, key, arr):
        if root is None:
            return False

        arr.append(root.val)

        if root.val == key:
            return True

        if self.findpath(root.left, key, arr):
            return True

        if self.findpath(root.right, key, arr):
            return True

        else:
            arr.pop()
        return False

    def solve(self, A, B):
        if A is None:
            return
        arr = []
        print(self.findpath(A, B, arr))
        # arr.append(root.val)
        print(arr)


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

s = Solution()
s.solve(root, 14)
