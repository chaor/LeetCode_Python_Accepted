# 2016-02-16  71 tests, 96 ms
# Thanks to https://leetcode.com/discuss/85976/short-python-solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(node):
            # N is the size of the largest BST in the tree.
            # If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
            # If the tree is a BST, then min and max are the minimum/maximum value in the tree.
            if not node: return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = check(node.left)
            N2, n2, min2, max2 = check(node.right)
            n = n1 + 1 + n2 if max1 < node.val < min2 else float('-inf')
            return max(N1, N2, n), n, min(min1, node.val), max(max2, node.val)
        return check(root)[0]
