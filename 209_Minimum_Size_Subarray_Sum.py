# 2015-06-27  Runtime: 52 ms
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        Sum, minLen, j = 0, len(nums) + 1, 0
        for i in xrange(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                minLen = min(minLen, i - j + 1)
                Sum -= nums[j]
                j += 1
        return 0 if minLen == len(nums) + 1 else minLen