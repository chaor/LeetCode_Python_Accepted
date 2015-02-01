# 2015-02-01  Runtime: 41 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        cur, res, stack = root, [], []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            poped = stack.pop()
            res.append(poped.val)
            cur = poped.right
        return res