# 2015-11-06  Runtime: 48 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        Q, res = collections.deque([root]), []
        while Q:
            res.append(Q[-1].val)
            for i in range(len(Q)):
                x = Q.popleft()
                if x.left:
                    Q.append(x.left)
                if x.right:
                    Q.append(x.right)
        return res