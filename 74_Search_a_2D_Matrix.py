# 2015-06-19  Runtime: 40 ms
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        L, R = 0, len(matrix) * len(matrix[0]) - 1
        while L <= R:
            M = (L + R) / 2
            row, col = M / len(matrix[0]), M % len(matrix[0])
            if matrix[row][col] == target: return True
            if matrix[row][col] < target:
                L = M + 1
            else:
                R = M - 1
        return False