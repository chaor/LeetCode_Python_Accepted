# 2015-05-19  Runtime: 44 ms

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix: return []
        rows, cols = len(matrix), len(matrix[0])
        direct = ((0, 1), (1, 0), (0, -1), (-1, 0)) # go right, go down, go left, go up
        currRow, currCol, currDirect, result = 0, -1, 0, [] # at first we go right
        while True:
            for i in xrange(cols):
                currRow, currCol = currRow + direct[currDirect][0], currCol + direct[currDirect][1]
                result.append(matrix[currRow][currCol])
            rows -= 1
            if rows == 0: break
            currDirect = (currDirect + 1) % 4 # change direction
            for i in xrange(rows):
                currRow, currCol = currRow + direct[currDirect][0], currCol + direct[currDirect][1]
                result.append(matrix[currRow][currCol])
            cols -= 1
            if cols == 0: break
            currDirect = (currDirect + 1) % 4 # change direction
        return result