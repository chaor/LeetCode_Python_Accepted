# 2015-11-08  Runtime: 100 ms
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        nextFirst = root
        while nextFirst:
            prev, nextFirst, curr = None, None, nextFirst
            while curr:
                if not nextFirst:
                    nextFirst = curr.left if curr.left else curr.right
                if curr.left:
                    if prev: prev.next = curr.left
                    prev = curr.left
                if curr.right:
                    if prev: prev.next = curr.right
                    prev = curr.right
                curr = curr.next  