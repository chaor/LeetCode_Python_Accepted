# 2016-03-22  21 tests, 48 ms
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat, x, y, dx, dy, number = [[0] * n for i in xrange(n)], -1, 0, 1, 0, 0
        for step in [i / 2 for i in xrange(2 * n, 1, -1)]:
            for j in xrange(step):
                x, y, number = x + dx, y + dy, number + 1
                mat[y][x] = number
            dx, dy = -dy, dx # turn right
        return mat
