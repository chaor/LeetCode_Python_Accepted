# 2015-10-13   Runtime: 68 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1: return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        num, p = 0, head
        pre, cur, nex = dummyHead, None, None
        while p:
            num, p = num + 1, p.next
        while num >= k:
            cur, nex = pre.next, pre.next.next
            for i in xrange(k - 1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            num -= k
        return dummyHead.next