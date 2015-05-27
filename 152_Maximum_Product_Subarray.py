# 2015-05-27  Runtime: 60 ms

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        # let fk = maxProduct whose end index is k, gk = minProduct whose end index is k
        # if current element > 0, fk * current will be next maxProduct, otherwise gk * current will be next maxProduct
        Max, fk, gk = nums[0], nums[0], nums[0]
        for i in xrange(1, len(nums)):
            fk, gk = max(fk * nums[i], nums[i], gk * nums[i]), min(fk * nums[i], nums[i], gk * nums[i])
            Max = max(Max, fk)
        return Max