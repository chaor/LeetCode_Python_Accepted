# 2016-03-26   43 tests, 52 ms
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # initialization
        dp = [[0] * n for i in xrange(m)]
        for i in xrange(m):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1
        for j in xrange(n):
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1
        # dp
        for i in xrange(1, m):
            for j in xrange(1, n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
