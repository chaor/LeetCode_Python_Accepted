# 2015-05-19  Runtime: 52 ms

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        # ones, twos, threes represent the ith bit had appeared once, twice, three times
        ones, twos, threes = 0, 0, 0
        for i in xrange(len(nums)):
            twos |= ones & nums[i]
            ones ^= nums[i]
            threes = ones & twos
            # When the ith bit had appeared for the third time, clear the ith bit of both ones and twos to 0.
            ones &= ~threes
            twos &= ~threes
        return ones