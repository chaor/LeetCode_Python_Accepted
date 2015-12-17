# 2015-12-16   38 tests, 60 ms
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res, i1, i2, same = len(words), len(words), - len(words), word1 == word2
        for i in range(len(words)):
            if words[i] == word1:
                if same:
                    i1, i2 = i2, i
                else:
                    i1 = i
            elif words[i] == word2:
                i2 = i
            res = min(res, abs(i1 - i2))
        return res