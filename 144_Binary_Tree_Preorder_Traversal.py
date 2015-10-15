# 2015-10-14 Runtime: 40 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack, result = [root], []
        while stack:
            x = stack.pop()
            result.append(x.val)
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        return result