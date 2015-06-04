# 2015-06-04  Runtime: 100 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) < 2: return len(nums)
        slow = 1
        for fast in xrange(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow