# 2015-08-30  Runtime: 44 ms
class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix: return []
        i, j, di, dj, M, N, res = 0, 0, 0, 1, len(matrix), len(matrix[0]), []
        while True:
            res.append(matrix[i][j])
            if len(res) == M * N: return res
            matrix[i][j] = None
            if matrix[(i + di) % M][(j + dj) % N] is None:
                di, dj = dj, -di # turn right
            i, j = i + di, j + dj