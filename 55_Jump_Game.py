# 2015-06-15  Runtime: 92 ms
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        maxReach = 0
        for i in xrange(len(nums)):
            if maxReach >= len(nums) - 1: return True
            if i <= maxReach:
                maxReach = max(maxReach, i + nums[i])
            else:
                return False