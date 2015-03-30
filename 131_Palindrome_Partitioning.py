# 2015-03-28  Runtime: 165 ms

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.res = []
        self.dfs(s, [])
        return self.res
        
    def dfs(self, s, L):
        if not s:
            self.res.append(L)
            return
        for i in xrange(1, len(s) + 1):
            word = s[:i]
            if word == word[::-1]:
                self.dfs(s[i:], L + [word])