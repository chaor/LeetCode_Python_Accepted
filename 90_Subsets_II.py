# 2015-06-20  Runtime: 92 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        res = set()
        for i in xrange(2 ** len(nums)):
            binary, subset = bin(i)[2:].zfill(len(nums)), ()
            for j in xrange(len(nums)):
                if binary[j] == '1': subset += (nums[j],)
            res.add(subset)
        return [list(s) for s in res]