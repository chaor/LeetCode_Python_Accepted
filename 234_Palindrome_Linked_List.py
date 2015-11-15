# 2015-11-14  Runtime: 21 tests, 144 ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head:
            return True
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next = self.reverseLinkedList(slow.next)
        slow = slow.next
        while slow:
            if head.val != slow.val:
                return False
            head, slow = head.next, slow.next
        return True
        
    def reverseLinkedList(self, h):
        pre, next = None, None
        while h:
            next = h.next
            h.next = pre
            pre = h
            h = next
        return pre