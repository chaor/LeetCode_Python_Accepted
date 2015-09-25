# 2015-09-24  Runtime: 112 ms
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        self.inorder, self.postorder = inorder, postorder
        return self.build(0, len(self.inorder) - 1, 0, len(self.postorder) - 1)
        
    def build(self, L1, R1, L2, R2):
        if L1 > R1: return None
        node = TreeNode(self.postorder[R2])
        if L1 == R1: return node
        ind = self.inorder.index(self.postorder[R2])
        node.left = self.build(L1, ind - 1, L2, L2 + ind - 1 - L1)
        node.right = self.build(ind + 1, R1, L2 + ind - L1, R2 - 1)
        return node