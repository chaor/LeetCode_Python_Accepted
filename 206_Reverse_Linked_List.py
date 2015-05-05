# 2015-05-05  recursive runtime: 88 ms, 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head: return None
        return self.recursiveReverse(head)[0]
    
    # @param {ListNode} n
    # @return {ListNode, ListNode} head, tail
    def recursiveReverse(self, node):
        if not node.next: return node, node
        head, tail = self.recursiveReverse(node.next)
        tail.next, node.next = node, None
        return head, node

# 2015-05-05  iterative runtime: 82 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        newHead = None
        while head:
            nextNode = head.next
            head.next = newHead
            newHead = head
            head = nextNode
        return newHead