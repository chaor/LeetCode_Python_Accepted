# 2015-06-20  Runtime: 412 ms
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        self.b, self.w, self.m, self.n, self.wLen = board, word, len(board), len(board[0]), len(word)
        for i in xrange(self.m):
            for j in xrange(self.n):
                if self.isFound(0, i, j):
                    return True
        return False

    def isFound(self, k, x, y):
        if x < 0 or y < 0 or x >= self.m or y >= self.n or self.b[x][y] == '.' or self.b[x][y] != self.w[k]:
            return False
        if k == self.wLen - 1:
            return True
        tmp, self.b[x][y] = self.b[x][y], '.'
        if self.isFound(k + 1, x - 1, y) or self.isFound(k + 1, x + 1, y) or \
                self.isFound(k + 1, x, y - 1) or self.isFound(k + 1, x, y + 1):
            return True
        self.b[x][y] = tmp
        return False