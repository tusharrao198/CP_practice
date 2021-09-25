# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer

    def solve(self, root, k, arr, s):
        if not root:
            return False

        arr.append(root.val)
        s[0] += root.val
        # print("ss ", arr, s)

        if s[0] == k:
            return True

        if s[0] > k:
            s[0] -= arr.pop()
            return False

        if self.solve(root.left, k, arr, s):
            return True

        if self.solve(root.right, k, arr, s):
            return True

        else:
            # print(arr, s)
            s[0] -= arr.pop()
            return False

    def hasPathSum1(self, A, B):
        if A is None:
            return
        arr = []
        s = [0]
        self.solve(A, B, arr, s)
        if s[0] == B:
            return 1
        return 0

    def hasPathSum(self, A, B):
        if not A:
            return 0
        print(A.val, B)
        if A.left is None and A.right is None and abs(A.val - B) == 0:
            return 1

        return self.hasPathSum(A.left, B - A.val) or self.hasPathSum(A.right, B - A.val)


# root = Node(10)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(7)
# root.left.right = Node(8)
# root.right.right = Node(15)
# root.right.left = Node(12)
# root.right.right.left = Node(14)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.left.right = Node(5)


s = Solution()
print(s.hasPathSum(root, 3))
