# 2015-06-04  Runtime: 56 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        dummyHead = ListNode(0)
        dummyHead.next = head
        p1_pre, p1, p2 = dummyHead, head, head
        for i in xrange(n): p2 = p2.next
        while p2:
            p1_pre, p1, p2 = p1_pre.next, p1.next, p2.next
        p1_pre.next = p1.next
        return dummyHead.next