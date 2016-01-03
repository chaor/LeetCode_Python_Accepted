# 2016-01-02  57 tests, 52 ms
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = [i for i, row in enumerate(grid) for v in row if v]
        y = [j for j in range(len(grid[0])) for row in grid if row[j]]
        midX, midY = x[len(x) / 2], y[len(y) / 2]
        return sum(abs(midX - i) + abs(midY - j) for i, row in enumerate(grid) for j, v in enumerate(row) if v)
