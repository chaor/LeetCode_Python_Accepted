# 2015-08-16  Runtime: 80 ms
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        maxReach = 0
        for i in xrange(len(nums)):
            if i > maxReach: return False
            if i + nums[i] > maxReach: maxReach = i + nums[i]
        return True