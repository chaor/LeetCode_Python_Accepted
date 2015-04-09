class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        # use dfs to find connected islands and change them to waters
        res = 0
        self.grid = [[bit for bit in row] for row in grid]
        for i in xrange(len(self.grid)):
            for j in xrange(len(self.grid[0])):
                if self.grid[i][j] == '1':
                    res += 1
                    self.dfs(i, j)
        return res
        
    def dfs(self, i, j):
        self.grid[i][j] = '0'
        if i > 0 and self.grid[i - 1][j] == '1': self.dfs(i - 1, j)
        if i < len(self.grid) - 1 and self.grid[i + 1][j] == '1': self.dfs(i + 1, j)
        if j > 0 and self.grid[i][j - 1] == '1': self.dfs(i, j - 1)
        if j < len(self.grid[0]) - 1 and self.grid[i][j + 1] == '1': self.dfs(i, j + 1)