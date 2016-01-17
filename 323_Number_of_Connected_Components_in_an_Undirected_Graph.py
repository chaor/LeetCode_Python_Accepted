# 2016-01-17  45 tests, 64 ms
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xRoot, yRoot = find(x), find(y)
            if xRoot == yRoot: return 0
            parent[xRoot] = yRoot
            return 1

        parent = range(n)
        return n - sum(union(x, y) for x, y in edges)
