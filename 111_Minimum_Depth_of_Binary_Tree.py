# 2015-03-19 Runtime: 109 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root: 
            return 0
        self.minDep = 10 ** 10
        self.solve(root, 1)
        return self.minDep
        
    def solve(self, node, depth):
        if not (node.left or node.right):
            self.minDep = min(self.minDep, depth)
        if node.left:
            self.solve(node.left, depth + 1)
        if node.right:
            self.solve(node.right, depth + 1)