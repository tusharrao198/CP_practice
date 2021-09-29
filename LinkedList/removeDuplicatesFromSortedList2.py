# https: // www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

from collections import OrderedDict
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
		mp = OrderedDict()
		head = A
		while head != None:
			mp[head.val] = mp.get(head.val, 0) + 1
			head = head.next

		newhead = ListNode(0)
		ans = newhead
		for k, v in mp.items():
			if v == 1:
				newhead.next = ListNode(k)
				newhead = newhead.next
			else:
				continue
		return ans.next
