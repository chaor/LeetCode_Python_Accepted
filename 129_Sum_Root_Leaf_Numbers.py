# 2015-09-30  Runtime: 48 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        #self.d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        self.res = 0
        self.calc(root, 0)
        return self.res
        
    def calc(self, node, x):
        if not node.left and not node.right:
            self.res += 10 * x + node.val
            return
        if node.left:
            self.calc(node.left, 10 * x + node.val)
        if node.right:
            self.calc(node.right, 10 * x + node.val)