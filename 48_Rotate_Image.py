# 2015-06-16  Runtime: 52 ms
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        # clockwise rotate: reverse up to down, then swap the symmetry 
        matrix.reverse()
        for i in xrange(len(matrix)):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]