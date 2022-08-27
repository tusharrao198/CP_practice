
# Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: # My Solution
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = []
        # always remember in python variables don't update when passed 
        # in recursion
        
        def solve(root, data):
            if not root: return
            
            data += str(root.val) 

            if root.left: solve(root.left, data)
            if root.right: solve(root.right, data)
            if not root.left and not root.right: ans.append(data)

        solve(root, data = '')
        return sum([int(i, 2) for i in ans])

    # leetcode Solution with stack iterative approach
    def sumRootToLeaf(self, root: TreeNode) -> int:
            root_to_leaf = 0
            stack = [(root, 0) ]
            
            while stack:
                root, curr_number = stack.pop()
                if root is not None:
                    curr_number = (curr_number << 1) | root.val
                    # if it's a leaf, update root-to-leaf sum
                    if root.left is None and root.right is None:
                        root_to_leaf += curr_number
                    else:
                        stack.append((root.right, curr_number))
                        stack.append((root.left, curr_number))
                            
            return root_to_leaf