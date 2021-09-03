
class TreeNode:
    
    def __init__(self, val):
        self.right = self.left = None
        self.val = val

bt = TreeNode(5) 
left = TreeNode(1)
right = TreeNode(6)

bt.left = left
bt.right = right
