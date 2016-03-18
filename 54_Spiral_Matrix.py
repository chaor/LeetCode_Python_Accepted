# 2016-03-18  22 tests, 44 ms
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        rows, cols, result = len(matrix), len(matrix[0]), []
        N, x, y, dx, dy = rows * cols, -1, 0, 1, 0
        while True:
            for i in xrange(cols):
                x, y = x + dx, y + dy
                result += matrix[y][x],
            rows -= 1
            if not rows: return result
            dx, dy = -dy, dx
            for i in xrange(rows):
                x, y = x + dx, y + dy
                result += matrix[y][x],
            cols -= 1
            if not cols: return result
            dx, dy = -dy, dx
