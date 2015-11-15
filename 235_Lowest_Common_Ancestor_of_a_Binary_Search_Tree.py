# 2015-11-14  Runtime: 120 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return root
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val <= root.val <= q.val:
                return root
            root = root.left if q.val < root.val else root.right
        return None