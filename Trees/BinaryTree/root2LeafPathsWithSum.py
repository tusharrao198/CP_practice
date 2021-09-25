# https://www.interviewbit.com/problems/root-to-leaf-paths-with-sum/


# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# simple approach
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers

    def pathSum(self, A, B):
        self.result = []
        self.helper(A, B, [], 0)
        return self.result

    def helper(self, root, target, path, currentSum):
        if not root:
            return

        if not root.left and not root.right and currentSum + root.val == target:
            self.result.append(path + [root.val])
            return

        if root.left:
            self.helper(root.left, target, path + [root.val], currentSum + root.val)
        if root.right:
            self.helper(root.right, target, path + [root.val], currentSum + root.val)


# -----------------------------------------------------------------------
# Alternate Solution
# first find all the leaf nodes whose path nodes csum up to given value
# and then finding path using findpath function when leaf node is given
# working but didn't get submitted on interviewbit
# Time complexity:
# 1. first for find ing leaf nodes : O(n)
# 2. and then finding path with those leafnodes


class Solution1:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def findpath(self, root, leaf, arr):
        if not root:
            return
        arr.append(root.val)
        if root.val == leaf and root.left == None and root.right == None:
            return True

        if self.findpath(root.left, leaf, arr):
            return True
        if self.findpath(root.right, leaf, arr):
            return True
        else:
            arr.pop()
        return False

    def pathSumMain(self, root, s, arr):
        if not root:
            return

        if root.left == None and root.right == None and abs(root.val - s) == 0:
            arr.append(root.val)
            print(arr)
            return True

        l = self.pathSumMain(root.left, s - root.val, arr)
        r = self.pathSumMain(root.right, s - root.val, arr)

        return l or r

    def pathSum(self, A, B):
        arr = []
        self.pathSumMain(A, B, arr)
        # return arr
        print(arr)

        ans = []
        for i in arr:
            temp = []
            self.findpath(A, i, temp)
            ans.append(temp)
        return ans


root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)

root.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(1)

s = Solution()
print(s.pathSum(root, 22))
