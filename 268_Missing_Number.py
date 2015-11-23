# 2015-11-22  Runtime: 68 ms
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        res = N
        for i in range(N):
            res ^= i ^ nums[i]
        return res