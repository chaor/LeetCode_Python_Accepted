# 2015-08-12  Runtime: 68 ms
class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # check rows
        for row in board:
            s = set()
            for char in row:
                if char == '.': continue
                if char in s: return False
                s.add(char)
        # check columns
        for i in xrange(9):
            s = set()
            for j in xrange(9):
                if board[j][i] == '.': continue
                if board[j][i] in s: return False
                s.add(board[j][i])
        # check 3x3 squares
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                s = set()
                for m in (0, 1, 2):
                    for n in (0, 1, 2):
                        if board[i + m][j + n] == '.': continue
                        if board[i + m][j + n] in s: return False
                        s.add(board[i + m][j + n])
        return True