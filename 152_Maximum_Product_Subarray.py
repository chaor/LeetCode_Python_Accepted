# 2014-12-23  Runtime: 196 ms
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        # dynamic programming, let dp[i] be the (max product, min product) of subarray ends in A[i]
        # we need min product each step because of +/- sign
        # 动态规划，让dp[i]表示以A[i]结尾的子数组的(最大乘积,最小乘积)
        # 由于正负号的问题，我们也需要记录每一次的最小乘积
        lenA, res = len(A), A[0]
        dpMax, dpMin = [A[0] for i in xrange(lenA)], [A[0] for i in xrange(lenA)]
        for i in xrange(1, lenA):
            t = (A[i], dpMax[i - 1] * A[i], dpMin[i - 1] * A[i])
            dpMax[i], dpMin[i] = max(t), min(t)
            res = max(res, dpMax[i])
        return res