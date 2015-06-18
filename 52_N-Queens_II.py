# 2015-06-17  Runtime: 112 ms
class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        # e.g. n = 4, a board [1, 3, 0, 2] means queens are at [0][1], [1][3], [2][0], [3][2]
        self.count, self.board, self.n = 0, [-1 for i in xrange(n)], n
        self.solve(0)
        return self.count
        
    def solve(self, rowNum):
        if rowNum == self.n:
            self.count += 1
            return
        availableColumn = [i for i in xrange(self.n)]
        # for the new row, make sure there's no column conflict
        for i in xrange(rowNum): availableColumn.remove(self.board[i])
        # for the new row, make sure there's no diagonal conflict
        for col in availableColumn[:]: # make a copy of availableColumn because we will delete some elements in iteration
            for i in xrange(rowNum):
                if col in availableColumn and abs(i - rowNum) == abs(self.board[i] - col): availableColumn.remove(col)
        # now all values in availableColumn is OK to put a Queen
        for col in availableColumn:
            self.board[rowNum] = col
            self.solve(rowNum + 1)