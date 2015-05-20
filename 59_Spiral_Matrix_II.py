# 2015-05-19  Runtime: 52 ms
class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0: return []
        matrix = [[None for i in xrange(n)] for j in xrange(n)]
        rows, cols = n, n
        direct = ((0, 1), (1, 0), (0, -1), (-1, 0)) # go right, go down, go left, go up
        currRow, currCol, currDirect, number = 0, -1, 0, 1 # at first we go right
        while True:
            for i in xrange(cols):
                currRow, currCol = currRow + direct[currDirect][0], currCol + direct[currDirect][1]
                matrix[currRow][currCol] = number
                number += 1
                if number > n * n: return matrix
            rows -= 1
            currDirect = (currDirect + 1) % 4 # change direction
            for i in xrange(rows):
                currRow, currCol = currRow + direct[currDirect][0], currCol + direct[currDirect][1]
                matrix[currRow][currCol] = number
                number += 1
                if number > n * n: return matrix
            cols -= 1
            currDirect = (currDirect + 1) % 4 # change direction