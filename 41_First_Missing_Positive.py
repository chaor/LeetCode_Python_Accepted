# 2015-06-13  Runtime: 56 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        # put the number into the right place, e.g. 5 should be put in nums[4], 1 should be put in nums[0]
        for i in xrange(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in xrange(len(nums)):
            if nums[i] != i + 1: return i + 1
        return len(nums) + 1