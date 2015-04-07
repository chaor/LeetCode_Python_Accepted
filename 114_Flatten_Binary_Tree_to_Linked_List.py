# 2015-04-07  Runtime: 75 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        # eliminate each level's root's left child
        while root:
            if root.left:
                p = root.left
                while p.right: p = p.right
                p.right = root.right
                root.right = root.left
                root.left = None
            root = root.right