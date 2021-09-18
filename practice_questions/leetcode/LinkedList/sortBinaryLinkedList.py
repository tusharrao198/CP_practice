# https://www.interviewbit.com/problems/sort-binary-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list

    def count(self, A, x):
        head = A
        count = 0
        while head:
            if head.val == x:
                count += 1
            head = head.next
        return count

    def solve1(self, A):  # O(1)
        count0 = self.count(A, 0)
        count1 = self.count(A, 1)

        new_head = A
        while A and count0 > 0:
            if A.val != 0:
                A.val = 0
            A = A.next
            count0 -= 1

        while A and count1 > 0:
            if A.val != 1:
                A.val = 1
            A = A.next
            count1 -= 1
        return new_head

    def solve(self, A):  # O(n)
        count0 = self.count(A, 0)
        count1 = self.count(A, 1)

        new = ListNode(-1)
        new_head = new

        while count0 > 0:
            new.next = ListNode(0)
            new = new.next
            count0 -= 1

        while count1 > 0:
            new.next = ListNode(1)
            new = new.next
            count1 -= 1

        return new_head.next
