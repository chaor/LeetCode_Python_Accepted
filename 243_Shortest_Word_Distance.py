# 2015-11-28  26 tests, 52 ms
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res, i1, i2 = len(words), 2 * len(words), 3 * len(words)
        for i, word in enumerate(words):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            res = min(res, abs(i1 - i2))
        return res