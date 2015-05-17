# 2015-05-17  Runtime: 88 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        # -1 means unbalanced
        return self.maxDepth(root) != -1
        
    def maxDepth(self, node):
        if not node: return 0
        L = self.maxDepth(node.left)
        if L == -1: return -1
        R = self.maxDepth(node.right)
        if R == -1: return -1
        return max(L, R) + 1 if abs(L - R) <= 1 else -1