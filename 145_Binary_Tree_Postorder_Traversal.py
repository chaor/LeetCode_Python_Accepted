# 2015-10-14  Runtime: 40 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # post order is Left->right->root
        # we can do root->right->left, then reverse the result list
        if not root: return []
        stack, result = [root], []
        while stack:
            x = stack.pop()
            result.append(x.val)
            if x.left:
                stack.append(x.left)
            if x.right:
                stack.append(x.right)
        return result[::-1]