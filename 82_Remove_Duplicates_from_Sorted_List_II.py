# 2015-06-23  Runtime: 96 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre, curr = dummyHead, dummyHead.next
        while curr:
            if curr.next and curr.next.val == curr.val:
                tmp = curr
                while tmp and tmp.val == curr.val: tmp = tmp.next
                pre.next, curr = tmp, tmp
            else:
                pre, curr = pre.next, curr.next
        return dummyHead.next