# https://www.interviewbit.com/problems/reverse-link-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list

    def reverseBetween(self, A, B, C):
        if B == C:
            return A

        new_head = ListNode(0)
        new_head.next = A
        prev = new_head
        i = 1
        while i < B:
            prev = prev.next
            i += 1

        curr = prev.next
        next_ = curr.next
        while i < C:
            temp = next_.next
            next_.next = curr
            curr = next_
            next_ = temp
            i += 1
        # print(prev.val, curr.val, next_.val, temp.val)
        # print(prev.next.val, prev.next.next.val)
        prev.next.next = next_
        prev.next = curr
        return new_head.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

s = Solution()
m, n = 2, 4
print(s.reverseBetween(node, m, n))
