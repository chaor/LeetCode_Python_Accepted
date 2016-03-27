# 2016-03-26   230 tests, 64 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        n, p1, p2 = 0, head, head
        # p1 goes to the last node
        while p1.next: n, p1 = n + 1, p1.next
        if k % (n + 1) == 0: return head
        # p2 goes to the k place
        for i in xrange(n - k % (n + 1)): p2 = p2.next
        # find new head
        new_head, p2.next, p1.next = p2.next, None, head
        return new_head
