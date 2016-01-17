# 2016-01-16  70 tests, 480 ms
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N, n = len(nums), [1] + nums + [1]
        dp = [[0] * (N + 2) for _ in range(N + 2)]
        for step in range(N):
            for s in range(1, N - step + 1):
                e = s + step
                dp[s][e] = max(dp[s][k - 1] + n[s - 1] * n[k] * n[e + 1] + dp[k + 1][e] for k in range(s, e + 1))
        return dp[1][N]
