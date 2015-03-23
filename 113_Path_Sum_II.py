# 2015-03-23  Runtime: 118 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        self.res = []
        self.dfs(root, sum, [])
        return self.res
        
    def dfs(self, node, sum, path):
        if not (node.left or node.right):
            if node.val == sum:
                self.res.append(path + [node.val])
            return
        if node.left:
            self.dfs(node.left, sum - node.val, path + [node.val])
        if node.right:
            self.dfs(node.right, sum - node.val, path + [node.val])