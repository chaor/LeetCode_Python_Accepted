# 2015-06-12  Runtime: 60 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root: return None
        L, R = self.invertTree(root.left), self.invertTree(root.right)
        root.left, root.right = R, L
        return root