# 2015-06-19  Runtime: 68 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if not nums: return []
        res = []
        nums.sort()
        # use binary, for [1,2,3], '010' means [2], '101' means [1,3]
        for i in xrange(2 ** len(nums)):
            # for binary, don't forget to add leading zeros to make sure it has len(nums) digits
            binary, subset = bin(i)[2:].zfill(len(nums)), []
            for j in xrange(len(nums)):
                if binary[j] == '1': subset.append(nums[j])
            res.append(subset)
        return res