# 2015-04-08  Runtime: 102 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.check(root, -10**10, 10**10)
        
    def check(self, node, lowerBound, upperBound):
        if not node:
            return lowerBound < upperBound
        return lowerBound < node.val < upperBound and self.check(node.left, lowerBound, node.val) and self.check(node.right, node.val, upperBound)