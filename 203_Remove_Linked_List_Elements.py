# 2015-11-07  Runtime: 104 ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        prev, cur = dummyHead, head
        while cur:
            if cur.val == val:
                prev.next, cur = cur.next, cur.next
            else:
                prev, cur = cur, cur.next
        return dummyHead.next