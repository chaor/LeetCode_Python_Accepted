# 2015-09-12  Runtime: 60 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, bits = [], len(nums)
        for i in xrange(2 ** bits):
            subset = []
            for j in xrange(bits):
                if i & 1: subset.append(nums[j])
                i >>= 1
            res.append(subset)
        return res