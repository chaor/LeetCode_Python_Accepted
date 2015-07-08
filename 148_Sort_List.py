# 2015-07-08  Runtime: 1896 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next: return head
        fast, slow = head.next.next, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        h2 = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(h2))

    @staticmethod
    def merge(h1, h2):
        dummyHead = ListNode(0)
        c = dummyHead
        while h1 and h2:
            if h1.val < h2.val:
                c.next = h1
                h1 = h1.next
            else:
                c.next = h2
                h2 = h2.next
            c = c.next
        if h1: c.next = h1
        if h2: c.next = h2
        return dummyHead.next