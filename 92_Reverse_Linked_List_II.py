# 2015-06-24  Runtime: 48 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        # thanks to https://leetcode.com/discuss/25580/simple-java-solution-with-clear-explanation
        if not head: return None
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead
        for i in xrange(m - 1): pre = pre.next
        start, then = pre.next, pre.next.next
        #  1  ->  2  ->  3  ->  4  ->  5
        # pre   start   then
        for i in xrange(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        # after first reverse:
        #  1  ->  3  ->  2  ->  4  ->  5
        # pre          start   then
        # 
        # after second reverse:
        #  1  ->  4  ->  3  ->  2  ->  5
        # pre                 start   then
        return dummyHead.next   