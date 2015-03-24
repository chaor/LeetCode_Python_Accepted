# 2014-03-24  Runtime: 120 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.dfs(root)[0]
        
    # @param node, a tree node
    # @return a tuple (whether current node is balanced(boolean), node's height(int)), 
    def dfs(self, node):
        if not node:
            return (True, 0)
        LisBalanced, Lheight = self.dfs(node.left)
        RisBalanced, Rheight = self.dfs(node.right)
        return (LisBalanced and RisBalanced and abs(Lheight -Rheight) <= 1, max(Lheight, Rheight) + 1)