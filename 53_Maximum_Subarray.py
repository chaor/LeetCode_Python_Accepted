# 2016-03-16, 201 tests, 56 ms
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('-inf')] + [None] * len(nums)
        for i, x in enumerate(nums):
            dp[i + 1] = max(dp[i] + x, x)
        return max(dp)


# 2015-05-27, divide and conquer, runtime: 164 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        # divide and conquer, the maximum subarray could either contain the middle element or not
        self.nums = nums
        return self.divideAndConquer(0, len(nums) - 1)

    def divideAndConquer(self, L, R):
        if L > R: return -10**10  # infinitesimal
        M = (L + R) / 2
        lResult, rResult = self.divideAndConquer(L, M - 1), self.divideAndConquer(M + 1, R)
        Sum, lMaxSum = 0, 0
        for i in reversed(xrange(L, M)):
            Sum += self.nums[i]
            lMaxSum = max(Sum, lMaxSum)
        Sum, rMaxSum = 0, 0
        for i in xrange(M + 1, R + 1):
            Sum += self.nums[i]
            rMaxSum = max(Sum, rMaxSum)
        return max(max(lResult, rResult), lMaxSum + self.nums[M] + rMaxSum)
