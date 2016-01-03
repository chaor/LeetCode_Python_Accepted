# 2016-01-03  54 tests, 188 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(node, cur, target):
            if not node:
                return 0
            cur = cur + 1 if node.val == target else 1
            self.maxLen = max(self.maxLen, cur)
            check(node.left, cur, node.val + 1)
            check(node.right, cur, node.val + 1)

        self.maxLen = 0
        if not root: return 0
        check(root, 0, root.val)
        return self.maxLen
