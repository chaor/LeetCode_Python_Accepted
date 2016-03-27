# 2016-03-26  61 tests, 76 ms
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # initialization 1st row and 1st column
        min_sum = [[0] * n for i in xrange(m)]
        min_sum[0][0] = grid[0][0]
        for i in xrange(1, m): min_sum[i][0] = min_sum[i - 1][0] + grid[i][0]
        for j in xrange(1, n): min_sum[0][j] = min_sum[0][j - 1] + grid[0][j]
        # dp
        for i in xrange(1, m):
            for j in xrange(1, n):
                min_sum[i][j] = grid[i][j] + min(min_sum[i - 1][j], min_sum[i][j- 1])
        return min_sum[m - 1][n - 1]
