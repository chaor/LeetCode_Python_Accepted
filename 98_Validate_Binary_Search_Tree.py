# 2015-09-23  Runtime: 80 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, -10 ** 10, 10 ** 10)
        
    def check(self, root, L, R):
        if not root: return True
        return self.check(root.left, L, root.val) and L < root.val < R and self.check(root.right, root.val, R) 

################Another Solution###################
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        # in-order traversal, check whether we got a strict monotonic increasing sequence
        self.prev = None
        return self.isMonotonicIncreasing(root)
        
    def isMonotonicIncreasing(self, p):
        if not p: return True
        if self.isMonotonicIncreasing(p.left):
            if self.prev and self.prev.val >= p.val: return False
            self.prev = p
            return self.isMonotonicIncreasing(p.right)
        return False