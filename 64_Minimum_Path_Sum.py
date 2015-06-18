# 2015-06-18  Runtime: 76 ms
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        M, N = len(grid), len(grid[0])
        # dp[x][y] is the min sum from grid[0][0] to grid[x][y]
        dp = [[0 for j in xrange(N)] for i in xrange(M)]
        dp[0][0] = grid[0][0]
        for i in xrange(1, M): dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in xrange(1, N): dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        for i in xrange(1, M):
            for j in xrange(1, N):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[M - 1][N - 1]