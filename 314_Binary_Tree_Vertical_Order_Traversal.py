# 2015-12-11  209 tests, 60 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        d = {}
        queue = collections.deque([(root, 0)])
        while queue:
            node, ind = queue.popleft()
            if ind not in d:
                d[ind] = [node.val]
            else:
                d[ind].append(node.val)
            if node.left:
                queue.append((node.left, ind - 1))
            if node.right:
                queue.append((node.right, ind + 1))
        return [d[key] for key in sorted(d.keys())]