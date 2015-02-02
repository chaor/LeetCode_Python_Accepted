# 2015-02-02  Runtime: 184 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head: return False
        fast, slow = head, head
        while True:
            fast = fast.next
            if not fast: return False
            fast = fast.next
            if not fast: return False
            slow = slow.next
            if fast == slow: return True