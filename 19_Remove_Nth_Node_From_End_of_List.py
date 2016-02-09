# 2016-02-09  Runtime: 52 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        p1, p2, dummyHead.next = dummyHead, dummyHead, head
        for i in range(n): p2 = p2.next
        while p2.next:
            p1, p2 = p1.next, p2.next
        p1.next = p1.next.next
        return dummyHead.next
