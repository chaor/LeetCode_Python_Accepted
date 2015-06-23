# 2015-06-22  Runtime: 104 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        p = head
        while p:
            if not p.next: break
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head