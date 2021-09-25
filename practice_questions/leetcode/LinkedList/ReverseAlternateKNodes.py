# https://www.interviewbit.com/problems/reverse-alternate-k-nodes/


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        current, prev, next_ = A, None, None
        count = 0
        # reversing
        while current != None and count < B:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
            count += 1

        if A != None:
            A.next = current

        skip = 0
        while current and skip < B - 1:
            current = current.next
            skip += 1

        if current:
            current.next = self.solve(current.next, B)

        return prev
