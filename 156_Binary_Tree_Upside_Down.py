# 2015-05-18  Runtime: 40 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def upsideDownBinaryTree(self, root):
        return self.dfsBottomUp(root, None)
        
    def dfsBottomUp(self, node, parent):
        if not node: return parent # the left-most leaf node will be finally returned 
        leftMostLeaf = self.dfsBottomUp(node.left, node)
        node.left = None if not parent else parent.right
        node.right = parent
        return leftMostLeaf