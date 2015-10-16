# 2015-10-15   Runtime: 360 ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = head
        while cur.next:
            if cur.val > cur.next.val:
                pPre, p = dummyHead, dummyHead.next
                while p.val < cur.next.val:
                    pPre, p = pPre.next, p.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = p
                pPre.next = tmp
            else:
                cur = cur.next
        return dummyHead.next