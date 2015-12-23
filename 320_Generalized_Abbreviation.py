# 2015-12-22  49 tests, 484 ms
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [""]
        self.res = []
        self.dfs(word, '')
        return self.res
    
    def dfs(self, s, oneAnswer):
        if not s:
            self.res.append(oneAnswer)
            return
        self.dfs(s[1:], oneAnswer + s[0])
        for i in range(1, len(s) + 1):
            if not oneAnswer or oneAnswer[-1].isalpha():
                self.dfs(s[i:], oneAnswer + str(i))