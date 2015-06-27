# 2015-06-27  Runtime: 176 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummyHead = ListNode(-10**10)
        dummyHead.next = head
        prev, curr = dummyHead, dummyHead.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return dummyHead.next