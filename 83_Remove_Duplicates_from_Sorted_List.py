# 2015-09-13  Runtime: 68 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0.1)
        dummyHead.next = head
        prev, curr = dummyHead, dummyHead.next
        while curr:
            if prev.val != curr.val:
                prev, curr = prev.next, curr.next
            else:
                curr = curr.next
                prev.next = curr
        return dummyHead.next