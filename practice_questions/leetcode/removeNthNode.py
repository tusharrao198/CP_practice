# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

## first approach
## nth from last means len(array) - n from beginning

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

    def count(self, head: ListNode) -> int:
        count_ = 0
        while head:
            count_ += 1
            head = head.next
        return count_

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        n = self.count(head) - n
        ans = ListNode(0)
        ans.next = head

        if ans is None:
            return
        if n == 0:
            head = ans.next
            # print(f'head = {head} and ans.next = {ans.next.val}')
            return ans.next.next

        count = 1
        prevnode = head
        while count < n:
            prevnode = prevnode.next
            count += 1
        prev_pos = count
        nextnode = prevnode.next.next
        prevnode.next = None
        prevnode.next = nextnode

        return ans.next


# second approach
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        first = ans
        second = ans

        for i in range(1, n + 2):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return ans.next
