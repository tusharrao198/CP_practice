# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        else:
            mid = len(nums) // 2
            left = self.sortedArrayToBST(nums[:mid])
            right = self.sortedArrayToBST(nums[mid + 1:])
            return TreeNode(nums[mid], left, right)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return head

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        return self.sortedArrayToBST(lst)

