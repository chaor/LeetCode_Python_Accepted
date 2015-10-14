# 2014-10-13  Runtime: 148 ms

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        self.s, self.wordDict, self.lenS = s, wordDict, len(s)
        # 使用matchable剪枝，matchable[j] == True指s[i:]可以被成功分成若干单词，
        self.matchable = [False for i in xrange(self.lenS)] + [True]
        for i in reversed(xrange(self.lenS)):
            for word in wordDict:
                if i + len(word) <= self.lenS and word == s[i: i + len(word)]:
                    self.matchable[i] = self.matchable[i] or self.matchable[i + len(word)]
        self.result = []
        self.dfs(0, '')
        return self.result
        
    def dfs(self, k, oneAnswer):
        if k >= len(self.s):
            self.result.append(oneAnswer[:-1])
            return
        for word in self.wordDict:
            if k + len(word) <= self.lenS and self.matchable[k + len(word)] and self.s[k: k + len(word)] == word:
                self.dfs(k + len(word), oneAnswer + word + ' ')