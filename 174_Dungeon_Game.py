2014-01-09  Runtime: 1408 ms

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        # Use 2D-array minHP[M][N] to record the possible min HP when knight reaches this point
        # A known fact is that when knight reaches bottom-right and after calculation, it's HP must >= 1
        # 用二维数组minHP[M][N]来记录骑士到达每个点时可能的最小生命值
        # 已知的可用于初始化的是在右下角的公主点，骑士到达并计算后，生命值应该>=1
        
        # initialization, 初始化
        M, N = len(dungeon), len(dungeon[0])
        minHP = [[10**5 for j in xrange(N)] for i in xrange(M)]
        minHP[M - 1][N - 1] = max(1, 1 - dungeon[M - 1][N - 1])
        
        # DP, 动态规划
        for i in reversed(xrange(M)):
            for j in reversed(xrange(N)):
                if i < M - 1: minHP[i][j] = min(minHP[i][j], minHP[i + 1][j] - dungeon[i][j])  
                if j < N - 1: minHP[i][j] = min(minHP[i][j], minHP[i][j + 1] - dungeon[i][j])
                minHP[i][j] = max(1, minHP[i][j])
        return minHP[0][0]