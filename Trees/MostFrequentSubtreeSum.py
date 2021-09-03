# https://leetcode.com/problems/most-frequent-subtree-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfstraversal(self, node, d, max_freq):
        if node is None:
            return 0

        # print(node.val)

        _sum = (
            node.val
            + self.dfstraversal(node.left, d, max_freq)
            + self.dfstraversal(node.right, d, max_freq)
        )

        d[_sum] = d.get(_sum, 0) + 1
        # print(node.val , d)

        max_freq[0] = max(max_freq[0], d[_sum])

        return _sum

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        max_freq = [0]

        self.dfstraversal(root, d, max_freq)

        ans = []
        for key in d:
            if d[key] == max_freq[0]:
                ans.append(key)

        return ans


# ----------------------------------------------------------------------------------------------------------

# duplicates not considered.
class Solution:
    def subtreeSum(self, root):
        if root is None:
            return 0
        return root.val + self.subtreeSum(root.left) + self.subtreeSum(root.right)

    # postorder traversal
    def pst(self, root, dd):
        if root is None:
            return 0
        self.pst(root.left, dd)
        self.pst(root.right, dd)
        dd[root.val] = self.subtreeSum(root)

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        global dd
        dd = {}
        self.pst(root, dd)
        print(dd)
        freq_vals = {}

        for k, v in dd.items():
            freq_vals[v] = freq_vals.get(v, 0) + 1

        freq_vals = {
            k: v for k, v in sorted(freq_vals.items(), key=lambda x: x[1], reverse=True)
        }

        vals = list(freq_vals.values())

        flag = False
        if len(vals) > 1 and vals[0] == vals[1]:
            flag = True

        if flag:
            ans = []
            x = vals[0]
            for k, v in freq_vals.items():
                if v == x:
                    ans.append(k)
            return ans
        else:
            return [next(iter(freq_vals))]
