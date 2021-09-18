# https://www.interviewbit.com/problems/intersection-of-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list

    def count(self, ll):
        head = ll
        count = 0
        while head is not None:
            head = head.next
            count += 1
        return count

    def getIntersectionNodeMain(self, head1, head2, diff):
        l1, l2 = head1, head2

        for i in range(diff):
            if l1 is None:
                return None
            l1 = l1.next

        while l1 is not None and l2 is not None:
            if l1 is l2:
                return l1

            l1 = l1.next
            l2 = l2.next

        return None

    def getIntersectionNode(self, A, B):
        c1 = self.count(A)
        c2 = self.count(B)

        if c1 > c2:
            return self.getIntersectionNodeMain(A, B, c1 - c2)
        else:
            return self.getIntersectionNodeMain(B, A, c2 - c1)
