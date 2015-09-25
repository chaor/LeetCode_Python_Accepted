# 2015-09-25  Runtime: 56 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, queue = [], collections.deque([root])
        while queue:
            level = []
            for i in xrange(len(queue)):
                x = queue.popleft()
                level.append(x.val)
                if x.left: queue.append(x.left)
                if x.right: queue.append(x.right)
            res.append(level)
        return res[::-1]