# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = head
        if temp is None:
            return
        while head and head.val == val:
            head = head.next
        cur = head
        prevnode = ListNode()
        prevnode.next = cur
        while cur is not None:
            if cur.val == val:
                nextnode = cur.next
                prevnode.next = None
                prevnode.next = nextnode
                cur = cur.next
            else:
                cur = cur.next
                prevnode = prevnode.next
        return head
