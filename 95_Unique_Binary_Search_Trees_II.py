# 2015-09-23  Runtime: 92 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.gen(range(1, n + 1))
        
    def gen(self, L):
        if not L: return [None]
        if len(L) == 1: return [TreeNode(L[0])]
        res = []
        for i in xrange(len(L)):
            for leftChild in self.gen(L[:i]):
                for rightChild in self.gen(L[i + 1:]):
                    res.append(TreeNode(L[i]))
                    res[-1].left, res[-1].right = leftChild, rightChild
        return res