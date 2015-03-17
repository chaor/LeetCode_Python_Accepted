# 2014-03-17  Runtime: 61 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        self.Sum = 0
        self.dfs(root, '')
        return self.Sum
    
    def dfs(self, node, s):
        if not (node.left or node.right):
            self.Sum += int(s + str(node.val))
            return
        if node.left:
            self.dfs(node.left, s + str(node.val))
        if node.right:
            self.dfs(node.right, s + str(node.val))
        return