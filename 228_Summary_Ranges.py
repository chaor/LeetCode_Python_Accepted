# 2015-06-25  Runtime: 48 ms
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) <= 1: return [str(i) for i in nums]
        nums.append(10**10) # infinity
        start, res = nums[0], []
        for i in xrange(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if nums[i-1] == start:
                    res.append(str(start))
                else:
                    res.append(str(start) + '->' + str(nums[i-1]))
                start = nums[i]
        return res