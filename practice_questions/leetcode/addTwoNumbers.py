import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        pointer = ans
        sum_ = carry = 0
        while l1 is not None or l2 is not None:
            sum_ = carry
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next

            carry = math.floor(sum_ / 10)
            pointer.next = ListNode(sum_ % 10)
            pointer = pointer.next

        if carry == 1:
            pointer.next = ListNode(carry)
        return ans.next
