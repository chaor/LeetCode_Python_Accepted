# 2015-06-25  Runtime: 172 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        # thanks to https://leetcode.com/discuss/13034/no-fancy-algorithm-just-simple-and-powerful-order-traversal
        self.prev, self.first, self.second = TreeNode(-10 ** 10), None, None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorder(self, node):
        if node.left: self.inorder(node.left)
        if not self.first and self.prev.val >= node.val:
            self.first = self.prev
        if self.first and self.prev.val >= node.val:
            self.second = node
        self.prev = node
        if node.right: self.inorder(node.right)