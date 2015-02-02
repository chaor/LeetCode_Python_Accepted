# 2015-02-02  Runtime: 177 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head: return None
        fast, slow = head, head
        while True:
            fast = fast.next
            if not fast: return None
            fast = fast.next
            if not fast: return None
            slow = slow.next
            if fast is slow:
                p = head
                while slow is not p:
                    p, slow = p.next, slow.next
                return p