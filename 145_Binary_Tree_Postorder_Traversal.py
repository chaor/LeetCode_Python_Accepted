# 2015-01-27  Runtime: 40 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root:
            return []
        else:
            res, stack, previousVisit = [], [root], 'Initial'
        while stack:
            stackTop = stack[-1]
            if (not stackTop.left and not stackTop.right) or previousVisit in (stackTop.right, stackTop.left):
                res.append(stackTop.val)
                previousVisit = stackTop
                stack.pop()
            else:
                if stackTop.right:
                    stack.append(stackTop.right)
                if stackTop.left:
                    stack.append(stackTop.left)
        return res