import math

# https://leetcode.com/problems/add-two-numbers-ii/submissions/

# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]

# same approach as in https://leetcode.com/problems/add-two-numbers/
# https://leetcode.com/problems/add-two-numbers/submissions/

# but here  most significant digit comes first
# so we reverse both list so that it would be easy for us to add carry to the next digit.

# again after getting answer we reverse to get the final number

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_
        return prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
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
        return self.reverseList(ans.next)
