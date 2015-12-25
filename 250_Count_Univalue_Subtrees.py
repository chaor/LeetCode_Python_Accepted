# 2015-12-25, merry christmas! 197 tests, 48 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.check(root)
        return self.count

    # return (isUnivalueTree, node.val)
    def check(self, node):
        if not node:
            return True, None
        leftIsUni, leftVal = self.check(node.left)
        rightIsUni, rightVal = self.check(node.right)
        isUni = leftIsUni and rightIsUni and \
            (not leftVal or node.val == leftVal) and (not rightVal or node.val == rightVal)
        if isUni:
            self.count += 1
        return isUni, node.val
