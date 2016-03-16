# 2016-03-16,  9 tests, 132 ms
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(board, row):
            if row == n: return 1
            count = 0
            for x in set_n - set(board):
                if all(row - i != abs(x - y) for i, y in enumerate(board[:row])):
                    board[row] = x
                    count += dfs(board, row + 1)
                    board[row] = '.'
            return count

        set_n = {i for i in xrange(n)}
        return dfs(['.'] * n, 0)
