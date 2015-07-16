# 2015-07-15  Runtime: 192 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        # thanks to https://leetcode.com/discuss/46104/simple-java-solution-in-o-n-without-extra-space
        result = [1 for i in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        right = 1
        for i in reversed(xrange(len(nums))):
            result[i] *= right
            right *= nums[i]
        return result