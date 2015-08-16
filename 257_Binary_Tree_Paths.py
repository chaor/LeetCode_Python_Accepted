# 2015-08-15  Runtime: 64 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root: return []
        self.result = []
        self.path(root, str(root.val))
        return self.result
        
    def path(self, node, s):
        if not (node.left or node.right):
            self.result.append(s)
        if node.left:
            self.path(node.left, s + '->' + str(node.left.val))
        if node.right:
            self.path(node.right, s + '->' + str(node.right.val))