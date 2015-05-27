# 2015-05-26  Runtime: 56 ms

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        matrix = [[0 for i in xrange(cols + 1)] for j in xrange(rows + 1)]
        # we use this to fill matrix[row - 1][cols - 1] with 1 in the first inner loop
        matrix[rows - 1][cols] = 1 
        for i in reversed(xrange(rows)):
            for j in reversed(xrange(cols)):
                matrix[i][j] = 0 if obstacleGrid[i][j] == 1 else matrix[i + 1][j] + matrix[i][j + 1]
        return matrix[0][0]