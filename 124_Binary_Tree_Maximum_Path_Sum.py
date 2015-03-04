# 2014-03-04  Runtime: 217 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxSum = -10**10
        self.dfs(root)
        return self.maxSum
        
    def dfs(self, node):
        # return maxPathSum only if current node is on the path
        if not node: return 0
        maxLeft = self.dfs(node.left)
        maxRight = self.dfs(node.right)
        self.maxSum = max(self.maxSum, maxLeft + node.val + maxRight)
        return max(0, maxLeft + node.val, node.val + maxRight)