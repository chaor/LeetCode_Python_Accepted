# 2016-01-05   158 tests, 380 ms
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        self.parent, islandCount, result = [i for i in range(m * n)], 0, []
        matrix = [[0] * n for i in range(m)]

        def find(x):
            if self.parent[x] != x:
                self.parent[x] = find(self.parent[x])
            return self.parent[x]

        def union(x, y):
            xRoot, yRoot = find(x), find(y)
            if xRoot == yRoot: return 0
            self.parent[xRoot] = yRoot
            return 1

        for i, j in positions:
            matrix[i][j], islandCount, idx = 1, islandCount + 1, i * n + j
            if i and         matrix[i - 1][j]: islandCount -= union(idx, idx - n)
            if i + 1 < m and matrix[i + 1][j]: islandCount -= union(idx, idx + n)
            if j and         matrix[i][j - 1]: islandCount -= union(idx, idx - 1)
            if j + 1 < n and matrix[i][j + 1]: islandCount -= union(idx, idx + 1)
            result.append(islandCount)
        return result
