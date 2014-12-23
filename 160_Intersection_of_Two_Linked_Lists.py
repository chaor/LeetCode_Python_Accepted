# 2014-12-20  Runtime: 1952 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    # Python version of https://oj.leetcode.com/discuss/17278/accepted-shortest-explaining-algorithm-comments-improvements
    # Thanks to satyakam
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        if not p1 or not p2: return None
        while p1 and p2 and p1 is not p2:
            p1, p2 = p1.next, p2.next
            if p1 is p2: return p1
            if not p1: p1 = headB
            if not p2: p2 = headA
        return p1