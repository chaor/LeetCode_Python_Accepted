# 2015-06-23  Runtime: 56 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        dummyHead1, dummyHead2 = ListNode(0), ListNode(0)
        p1, p2 = dummyHead1, dummyHead2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next, p2.next = dummyHead2.next, None
        return dummyHead1.next