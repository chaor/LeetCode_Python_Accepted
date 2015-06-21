# 2015-06-21  Runtime: 128 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        self.p, self.i = preorder, inorder
        return self.dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
        
    def dfs(self, L1, R1, L2, R2):
        if L1 > R1: return None
        if L1 == R1: return TreeNode(self.p[L1])
        # pos is the index of current root (preorder[L1]) in inorder list
        root, pos = TreeNode(self.p[L1]), self.i.index(self.p[L1])
        root.left = self.dfs(L1 + 1, L1 + pos - L2, L2, pos - 1)
        root.right = self.dfs(L1 + pos - L2 + 1, R1, pos + 1, R2)
        return root