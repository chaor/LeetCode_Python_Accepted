# 2015-09-25  Runtime: 100 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self.build(0, len(nums) - 1)
        
    def build(self, L, R):
        if L > R: return None
        if L == R: return TreeNode(self.nums[L])
        mid = (L + R) / 2
        node = TreeNode(self.nums[mid])
        node.left = self.build(L, mid - 1)
        node.right = self.build(mid + 1, R)
        return node