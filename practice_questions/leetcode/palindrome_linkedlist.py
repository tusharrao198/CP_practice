# https://leetcode.com/problems/palindrome-linked-list/

# https: // dev.to/seanpgallivan/solution-palindrome-linked-list-5721

# used https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare technique for cycle detection

# then used two pointers slow and fast. loop thorugh all the nodes with fast moving twice as fast as slow
# By the end of the loop, slow reaches at the middle and fast at the end.
# now from slow pointer we start reversing the array.

# Once the back half is properly reversed and slow is once again at the end of the list, we can now start 
# fast back over again at the head and compare the two halves simultaneously, with no extra space required.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev= slow
        slow = slow.next
        prev.next = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        fast = head
        slow = prev

        while slow:
            if slow.val!=fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True





s= Solution()

# arr = [1,2,2,1]
# x = s.isPalindrome(arr)

# print(x)
