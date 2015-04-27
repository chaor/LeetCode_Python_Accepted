# 2015-04-27  Runtime: 120 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1