# 2015-09-29  Runtime: 156 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.maxSum = -sys.maxint
        self.calc(root)
        return self.maxSum
        
    def calc(self, node):
        L, R = 0, 0
        if node.left:
            L = self.calc(node.left)
        if node.right:
            R = self.calc(node.right)
        self.maxSum = max(self.maxSum, L + node.val + R)
        return max(0, node.val, node.val + L, node.val + R)