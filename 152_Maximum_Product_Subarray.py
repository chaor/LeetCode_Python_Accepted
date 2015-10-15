# 2015-10-15  Runtime: 52 ms
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxP, minP, res = nums[0], nums[0], nums[0]
        for i in xrange(1, len(nums)):
            maxP, minP = max(nums[i], maxP * nums[i], minP * nums[i]), min(nums[i], maxP * nums[i], minP * nums[i])
            if maxP > res: res = maxP
        return res