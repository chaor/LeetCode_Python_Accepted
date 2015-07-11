# 2015-07-10  Runtime: 168 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        # thanks to https://leetcode.com/discuss/44959/3-lines-o-1-space-some-alternatives
        a, b = sorted([p.val, q.val])
        while not a <= root.val <= b:
            root = root.left if b < root.val else root.right
        return root