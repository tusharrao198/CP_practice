# https://www.interviewbit.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head):
        if not head or not head.next:
            return head

        prev = None
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow at middle and fast at the end

        prev.next = None
        prev = None
        current = slow
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        new_head = ListNode(-1)
        tail = new_head
        while head:
            next_ = head.next
            head.next = prev
            tail.next = head
            tail = prev
            head = next_
            prev = prev.next

        if prev:
            tail.next = prev
        return new_head.next
