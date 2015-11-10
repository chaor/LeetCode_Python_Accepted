# 2015-11-10  Runtime: 164 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return 1
        p1, p2, L, R = root.left, root.right, 0, 0
        while p1:
            p1, L = p1.left, L + 1
        while p2:
            p2, R = p2.left, R + 1
        if L == R:
            return 1 + 2 ** L - 1 + self.countNodes(root.right)
        else:
            return 1 + 2 ** R - 1 + self.countNodes(root.left)