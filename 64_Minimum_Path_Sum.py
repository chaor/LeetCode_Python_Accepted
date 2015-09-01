# 2015-08-31  Runtime: 76 ms
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        Sum = [[10 ** 10] * (N + 1) for i in xrange(M + 1)] # initialize to infinity
        Sum[M - 1][N] = 0
        for i in reversed(xrange(M)):
            for j in reversed(xrange(N)):
                Sum[i][j] = grid[i][j] + min(Sum[i + 1][j], Sum[i][j + 1])
        return Sum[0][0]