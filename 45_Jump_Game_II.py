# 2015-06-16  Runtime: 64 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        maxReach, nextMaxReach, jump = 0, 0, 0
        for i in xrange(len(nums) - 1):
            nextMaxReach = max(nextMaxReach, i + nums[i])
            if i == maxReach:
                jump, maxReach = jump + 1, nextMaxReach
        return jump