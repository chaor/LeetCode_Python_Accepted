# 2014-03-15, Runtime: 118 ms

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.s = s
        self.dict = dict
        # 使用matchable剪枝，matchable[j] == True指s[i:]可以被成功分成若干单词
        # use matchable to pruning, matchable[j] == True means s[i:] can be successfully seperated into several words
        self.matchable = [False for i in xrange(len(s) + 1)]
        self.matchable[len(s)] = True
        for i in reversed(xrange(len(s))):
            for word in dict:
                if i + len(word) <= len(s) and word == s[i:i+len(word)]:
                    self.matchable[i] = self.matchable[i] or self.matchable[i+len(word)]
        self.results = []
        self.dfs(0, [])
        return self.results
        
    def dfs(self, k, oneResult):
        if k >= len(self.s):
            self.results.append(' '.join(oneResult))
            return
        for word in self.dict:
            if k + len(word) <= len(self.s) and self.matchable[k + len(word)] and self.s[k:k+len(word)] == word:
                self.dfs(k + len(word), oneResult + [word])