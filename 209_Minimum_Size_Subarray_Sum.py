# 2015-08-23  Runtime: 52 ms
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        Sum, L, minLen = 0, 0, 10 ** 10 # infinity
        for R in xrange(len(nums)):
            Sum += nums[R]
            while Sum >= s:
                if R - L + 1 < minLen: minLen = R - L + 1
                Sum -= nums[L]
                L += 1
        return minLen if minLen != 10 ** 10 else 0