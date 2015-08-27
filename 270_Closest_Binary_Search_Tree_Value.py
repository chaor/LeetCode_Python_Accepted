# 2015-08-26  Runtime: 84 ms, recursively
# thanks to https://leetcode.com/discuss/54438/4-7-lines-recursive-iterative-ruby-c-java-python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        a = root.val
        kid = root.left if target < a else root.right
        if not kid: return a
        b = self.closestValue(kid, target)
        return a if abs(a - target) < abs(b - target) else 

# Runtime: 76 ms, iteratively
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:
            closest = closest if abs(closest - target) < abs(root.val - target) else root.val
            root = root.left if target < root.val else root.right
        return closest