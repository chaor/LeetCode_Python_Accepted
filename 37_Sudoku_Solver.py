# 2015-06-14  Runtime: 836 ms
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        self.board = board
        self.solve()
    
    # @return {boolean} True if a valid solution is found    
    def solve(self):
        for i in xrange(9):
            for j in xrange(9):
                if self.board[i][j] == '.':
                    for char in self.getFitCharList(i, j):
                        self.board[i][j] = char
                        if self.solve(): return True
                        self.board[i][j] = '.'
                    return False
        return True
    
    # @param {int} i
    # @param {int} j
    # @return {List} a list of available characters for board[i][j]
    def getFitCharList(self, m, n):
        L = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for char in self.board[m]:
            if char != '.': L.remove(char)
        for i in xrange(9):
            if self.board[i][n] != '.' and self.board[i][n] in L: L.remove(self.board[i][n])
        for i in (m / 3 * 3, m / 3 * 3 + 1, m / 3 * 3 + 2):
            for j in (n / 3 * 3, n / 3 * 3 + 1, n / 3 * 3 + 2):
                if self.board[i][j] != '.'and self.board[i][j] in L: L.remove(self.board[i][j])
        return L