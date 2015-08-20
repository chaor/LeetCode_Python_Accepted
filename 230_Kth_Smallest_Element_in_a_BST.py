# 2015-08-20   Runtime: 96 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        return self.find(root)
        
    def find(self, node):
        if node.left:
            x = self.find(node.left)
            if self.k == 0: return x
        self.k -= 1
        if self.k == 0: return node.val
        if node.right: return self.find(node.right)