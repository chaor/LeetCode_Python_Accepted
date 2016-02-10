# 2016-02-09   Runtime: 68 ms

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
        curr, dummyHead.next, rangeK, rangeK_1 = dummyHead, head, range(k), range(k - 1)
        while True:
            # count nodes, if < k then return
            p1, tail = curr, curr.next
            for i in rangeK:
                if p1.next: p1 = p1.next
                else: return dummyHead.next
            # reverse k nodes
            for i in rangeK_1:
                p2 = tail.next
                tail.next = p2.next
                p2.next = curr.next
                curr.next = p2
            # move k steps
            curr = tail
