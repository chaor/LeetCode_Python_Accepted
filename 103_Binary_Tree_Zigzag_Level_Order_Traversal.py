# 2015-04-14  Runtime: 69 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        self.res = []
        self.preOrder(root, 0)
        return self.res
    
    def preOrder(self, node, depth):
        if not node: return
        if len(self.res) == depth: self.res.append([])
        if depth % 2 == 0:
            self.res[depth].append(node.val)
        else:
            self.res[depth].insert(0, node.val)
        self.preOrder(node.left, depth + 1)
        self.preOrder(node.right, depth + 1)