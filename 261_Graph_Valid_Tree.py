# 2015-08-22  Runtime: 44 ms
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # thanks to https://leetcode.com/discuss/52610/8-10-lines-union-find-dfs-and-bfs
        # union-find algorithm
        parent = range(n)
        def find(x):
            return x if parent[x] == x else find(parent[x])
        def union(a, b):
            x, y = find(a), find(b)
            parent[x] = y
            return x != y
        return len(edges) == n - 1 and all([union(e[0], e[1]) for e in edges])