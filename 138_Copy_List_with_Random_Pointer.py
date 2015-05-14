# 2015-05-14  Runtime: 284 ms

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
        
        # put the copy of each node behind them
        p = head
        while p:
            next = p.next
            copy = RandomListNode(p.label)
            p.next = copy
            copy.next = next
            p = next
        
        # set the Node.random for the copy
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        
        # seperate this copy
        p = head
        headCopy = p.next if p else None
        while p:
            copy = p.next
            p.next = copy.next
            p = p.next
            copy.next = p.next if p else None
        return headCopy