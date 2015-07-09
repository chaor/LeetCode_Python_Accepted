# 2015-07-09  Runtime: 440 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        # thanks to https://leetcode.com/discuss/38944/time-limit-for-the-python-solution
        if not root: return 0
        h1, h2 = 0, 0
        node = root
        while node:
            h1, node = h1 + 1, node.left
        node = root
        while node:
            h2, node = h2 + 1, node.right
        if h1 == h2: return 2 ** h1 - 1
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)