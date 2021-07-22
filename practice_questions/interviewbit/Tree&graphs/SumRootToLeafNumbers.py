# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def solve(self, root,SUM):
        if not root:
            return 0
        SUM=SUM*10+root.val
        if not root.left and not root.right:
            return SUM
        else:
            return self.solve(root.left,SUM)+self.solve(root.right,SUM)
    def sumNumbers(self, A):
        SUM=0
        return self.solve(A,SUM)%1003


