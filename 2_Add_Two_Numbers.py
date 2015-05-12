# 2015-05-11  Runtime: 345 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        p, q, cur, carry = l1, l2, dummyHead, 0
        while p or q:
            x = 0 if not p else p.val
            y = 0 if not q else q.val
            cur.next = ListNode((x + y + carry) % 10)
            carry = (x + y + carry) / 10
            cur = cur.next
            if p: p = p.next
            if q: q = q.next
        if carry > 0: cur.next = ListNode(carry)
        return dummyHead.next