# 2015-09-23  Runtime: 140 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        curr, pre, preFirst, first, second, stack = root, TreeNode(-10 ** 10), None, None, None, []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val < pre.val:
                if not first:
                    first, preFirst = curr, pre
                else:
                    second = curr
            pre = curr    
            curr = curr.right
        if second:
            preFirst.val, second.val = second.val, preFirst.val
        else:
            preFirst.val, first.val = first.val, preFirst.val