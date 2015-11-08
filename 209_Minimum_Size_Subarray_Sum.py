# 2015-11-07  Runtime: 48 ms
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        Sum, L, minLen = 0, 0, sys.maxint
        for R in range(len(nums)):
            Sum += nums[R]
            while Sum >= s:
                minLen = min(minLen, R - L + 1)
                Sum -= nums[L]
                L += 1
        return minLen if minLen != sys.maxint else 0