# 2015-05-17  Runtime: 184 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        self.maxSum = -10 ** 10 # infinitesimal
        self.findMax(root)
        return self.maxSum
        
    def findMax(self, node):
        if not node: return 0
        LMax, RMax = self.findMax(node.left), self.findMax(node.right)
        self.maxSum = max(self.maxSum, LMax + node.val + RMax)
        ret = node.val + max(LMax, RMax)
        return ret if ret > 0 else 0