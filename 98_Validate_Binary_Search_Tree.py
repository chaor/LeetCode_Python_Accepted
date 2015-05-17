# 2015-05-17  Runtime: 76 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.check(root, None, None) # first None means infinitesimal, second None means infinite large
        
    def check(self, node, low, high):
        if not node: return True
        return (low == None or low < node.val) and (high == None or node.val < high) \
            and self.check(node.left, low, node.val) and self.check(node.right, node.val, high)

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