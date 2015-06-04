# 2015-06-04  Runtime: 80 ms
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        self.result, self.n, self.numbers = [], n, [i + 1 for i in xrange(n)]
        self.dfs([], 0, k)
        return self.result
        
    def dfs(self, L, start, k):
        if k == 0:
            self.result.append(L)
            return
        for i in xrange(start, self.n):
            self.dfs(L + [self.numbers[i]], i + 1, k - 1)