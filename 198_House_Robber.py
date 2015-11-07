# 2015-11-06  Runtime: 40 ms
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0: return 0
        if N == 1: return nums[0]
        dp = [nums[0], max(nums[0], nums[1])] + [0] * (N - 2)
        for i in range(2, N):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[N - 1]