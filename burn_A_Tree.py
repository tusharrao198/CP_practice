# Definition for a  binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer

    mx = float("-inf")

    def travel(self, root, level):
        if not root.left and not root.right:
            self.mx = max(self.mx, level)
            return -1

        if root.left:
            self.travel(root.left, level + 1)

        if root.right:
            self.travel(root.right, level + 1)

    def search(self, root, x, arr):
        if not root:
            return -1

        arr.append(root)

        if root.val == x:
            return 1

        elif self.search(root.left, x, arr):
            return 1

        elif self.search(root.right, x, arr):
            return 1

        else:
            arr.pop()

    def solve(self, A, B):
        arr = []
        self.search(A, B, arr)

        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                arr[i].left = None
            else:
                arr[i].right = None

        for i, node in enumerate(arr[::-1]):
            self.travel(node, i)
        return self.mx


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

s = Solution()
B = 4
ans = s.solve(root, B)
print(ans)


class Solution1:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def bottom_up(node, starting):
            if not node:
                return -1, False

            if node.val == starting:
                return 0, True

            time_left, burn_left = bottom_up(node.left, starting)
            time_right, burn_right = bottom_up(node.right, starting)

            burn = burn_left or burn_right
            if not burn:
                time = max(time_left, time_right)
            else:
                curr = time_left + time_right + 2
                if self.time < curr:
                    self.time = curr
                time = time_left if burn_left else time_right

            return time + 1, burn

        import sys

        sys.setrecursionlimit(10 ** 4)

        self.time = 0
        bottom_up(A, B)
        return self.time
