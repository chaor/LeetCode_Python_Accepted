# 2015-05-17  Runtime: 112 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        self.nums = nums
        return self.buildBST(0, len(nums) - 1)
        
    def buildBST(self, start, end):
        if start > end: return None
        mid = (start + end) / 2
        node = TreeNode(self.nums[mid])
        node.left = self.buildBST(start, mid - 1)
        node.right = self.buildBST(mid + 1, end)
        return node