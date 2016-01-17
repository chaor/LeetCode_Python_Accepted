# 2016-01-16   70 tests, 72 ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        evenHead = ListNode(0)
        p1, p2 = head, evenHead
        while p1 and p1.next:
            p2.next, p1.next = p1.next, p1.next.next
            if p1.next: p1 = p1.next
            p2 = p2.next
        p1.next = evenHead.next
        p2.next = None
        return head
