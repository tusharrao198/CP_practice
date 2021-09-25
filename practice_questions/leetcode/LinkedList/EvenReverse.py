# https://www.interviewbit.com/problems/even-reverse/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list

    def solve(self, A):
        odd, even = [], []
        count = 1
        new = A
        while A:
            if count % 2 == 0:
                even.append(A.val)
            else:
                odd.append(A.val)
            count += 1
            A = A.next

        cc = 1
        new_head = new
        while new and len(even) > 0:
            if cc % 2 == 0:
                new.val = even.pop()
            cc += 1
            new = new.next
        return new_head


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(5)
n.next.next.next.next.next = ListNode(6)

s = Solution()
print(s.solve(n))
