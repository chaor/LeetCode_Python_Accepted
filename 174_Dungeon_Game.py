# 2015-11-05  Runtime: 60 ms

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        M, N = len(dungeon), len(dungeon[0])
        dp = [[sys.maxint] * (N + 1) for i in range(M + 1)]
        dp[M - 1][N] = 1
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                # make sure knight's HP is at least 1
                dp[i][j] = max(1, min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j])
        return dp[0][0]