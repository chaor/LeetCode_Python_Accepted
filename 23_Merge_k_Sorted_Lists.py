# 2015-05-13  Runtime: 780 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists: return None
        end = len(lists) - 1
        while end > 0:
            start = 0
            while start < end:
                lists[start] = self.mergeTwoList(lists[start], lists[end])
                start, end = start + 1, end - 1
        return lists[0]
        
    # @param {ListNode, ListNode} l1 head, l2 head
    # @return {ListNode}
    def mergeTwoList(self, l1, l2):
        dummyHead = ListNode(0)
        p = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1: p.next = l1
        if l2: p.next = l2
        return dummyHead.next