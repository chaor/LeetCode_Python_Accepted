# 2015-06-26  Runtime: 172 ms
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        curr = root
        while curr:
            nextLevelFirstNode, prev = None, None
            while curr:
                if not nextLevelFirstNode:
                    nextLevelFirstNode = curr.left if curr.left else curr.right
                if curr.left:
                    if prev: prev.next = curr.left
                    prev = curr.left
                if curr.right:
                    if prev: prev.next = curr.right
                    prev = curr.right
                curr = curr.next
            curr = nextLevelFirstNode # go to next level    