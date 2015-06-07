# 2015-06-07   Runtime: 96 ms
# thanks to https://leetcode.com/discuss/21301/short-but-recursive-java-code-with-comments

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        p, count = head, 0
        while p and count < k: p, count = p.next, count + 1
        if count < k: return head
        curr = self.reverseKGroup(p, k)
        # reverse current k nodes
        for i in xrange(k):
            tmp = head.next
            head.next = curr
            curr = head
            head = tmp
        return curr