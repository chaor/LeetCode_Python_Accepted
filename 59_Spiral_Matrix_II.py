# 2015-08-30  Runtime: 64 ms
# thanks to https://leetcode.com/discuss/46720/4-9-lines-python-solutions
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        i, j, di, dj, m = 0, 0, 0, 1, [[0] * n for i in xrange(n)]
        for x in xrange(1, n * n + 1):
            m[i][j] = x
            if m[(i + di) % n][(j + dj) % n]: # if there's already a number in m, turn right
                di, dj = dj, -di
            i, j = i + di, j + dj
        return m