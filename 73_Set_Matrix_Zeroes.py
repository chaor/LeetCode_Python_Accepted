# 2015-06-16  Runtime: 177 ms
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        # thanks to https://leetcode.com/discuss/15997/any-shortest-o-1-space-solution
        # use the first row and first column to record state
        col0 = 1
        for i in xrange(len(matrix)):
            if matrix[i][0] == 0: col0 = 0
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 0: matrix[i][0], matrix[0][j] = 0, 0
        
        # now according to first row & first column's state, set matrix zeroes
        for i in reversed(xrange(len(matrix))):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0
            if col0 == 0: matrix[i][0] = 0