# 2015-05-11  Runtime: 57 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        dummyHead = ListNode(0)
        dummyHead.next, p, prev = head, head, dummyHead
        while p and p.next:
            # change p -> q -> r ... to q -> p -> r ...
            q, r = p.next, p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummyHead.next