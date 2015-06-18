# 2015-06-18  Runtime: 72 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        
        # get total length
        L = 0
        while fast.next: fast, L = fast.next, L + 1
        
        # get L - k % L th node
        for i in xrange(L - k % L): slow = slow.next
        
        # rotate
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next