# 2016-02-09  55 tests, 40 ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        p, dummyHead.next = dummyHead, head
        while p and p.next and p.next.next:
            p1, p2, p3 = p.next, p.next.next, p.next.next.next
            p.next, p1.next, p2.next = p2, p3, p1
            p = p1
        return dummyHead.next
