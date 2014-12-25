# 2014-12-25  Runtime: 928 ms  Merry Chirstmas! 圣诞节快乐!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next: return head
        # add a dummy node in head, 在链表头部加一个空节点
        dummy = ListNode(-10**4)
        dummy.next = head
        cur = head
        while cur.next:
            if cur.val > cur.next.val:
                # insert cur.next into proper position, note that head's position may change, but dummy's position is fixed
                # 把cur.next插入前面合适的位置，注意head所指的节点在链表中的位置会变，而dummy所指的节点在链表中的位置不变
                pPre, p = dummy, dummy.next
                while p.val < cur.next.val:
                    pPre, p = pPre.next, p.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = p
                pPre.next = tmp
            else:
                cur = cur.next
        return dummy.next