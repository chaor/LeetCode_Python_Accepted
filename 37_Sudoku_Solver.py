# 2015-08-12  Runtime: 1188 ms
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        self.b = board
        self.dfs()

    def dfs(self):
        for i in xrange(9):
            for j in xrange(9):
                if self.b[i][j] == '.':
                    s = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                    for m in xrange(9):
                        if self.b[i][m] in s:
                            s.remove(self.b[i][m])
                        if self.b[m][j] in s:
                            s.remove(self.b[m][j])
                    for m in (0, 1, 2):
                        for n in (0, 1, 2):
                            if self.b[i / 3 * 3 + m][j / 3 * 3 + n] in s:
                                s.remove(self.b[i / 3 * 3 + m][j / 3 * 3 + n])
                    for char in s:
                        l = [c for c in self.b[i]]
                        l[j] = char
                        self.b[i] = ''.join(l) 
                        if self.dfs(): return True
                        l = [c for c in self.b[i]]
                        l[j] = '.'
                        self.b[i] = ''.join(l)
                    return False
        return True