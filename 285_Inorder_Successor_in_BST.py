# 2015-09-22  Runtime: 116 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # thanks to https://leetcode.com/discuss/59728/10-lines-o-h-java-c
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        candidate = None
        while root != p:
            if p.val < root.val:
                candidate = root
                root = root.left
            else:
                root = root.right
        return candidate