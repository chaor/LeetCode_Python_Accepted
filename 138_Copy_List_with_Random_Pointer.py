# 2015-11-16  Runtime: 124 ms

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # put the copy of each node behind them, so that node.next.random = node.random.next
        # N1 -> N1' -> N2 -> N2' -> N3 -> N3' -> ...
        
        if not head: return None
        # put each node's copy behind it
        curr = head
        while curr:
            copy = RandomListNode(curr.label)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
            
        # set self.random for each node's copy
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # extract each node's copy to form a new linkedlist        
        headcopy, curr1, curr2 = head.next, head, head.next
        while curr2.next:
            curr1.next, curr2.next = curr1.next.next, curr2.next.next
            curr1, curr2 = curr1.next, curr2.next
        curr1.next = None
        return headcopy