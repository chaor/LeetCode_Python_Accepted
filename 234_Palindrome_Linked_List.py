# 2015-07-10  Runtime: 208 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
    	# thanks to https://leetcode.com/discuss/44751/11-lines-12-with-restore-o-n-time-o-1-space
        rev, fast = None, head
        # reverse the first half of the list, rev is the first node
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        # if total nodes N is even, fast will be None. If N is odd, fast will be the last node    
        tail = head.next if fast else head
        isPalin = True
        # update isPalin, recover the first half of the list
        while rev:
            isPalin = isPalin and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return isPalin