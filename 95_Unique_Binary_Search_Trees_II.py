# 2015-06-24  Runtime: 104 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.solve([i for i in xrange(1, n + 1)])
        
    def solve(self, L):
        if not L: return [None]
        if len(L) == 1: return [TreeNode(L[0])]
        res = []
        for i in xrange(len(L)):
            leftList, rightList = self.solve(L[:i]), self.solve(L[i + 1:])
            for left in leftList:
                for right in rightList:
                    root = TreeNode(L[i])
                    root.left, root.right = left, right
                    res.append(root)
        return res