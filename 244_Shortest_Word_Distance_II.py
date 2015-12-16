# 2015-12-16  11 tests, 112 ms
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dic, self.length = {}, len(words)
        for i, word in enumerate(words):
            self.dic[word] = self.dic.get(word, []) + [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res, i, j = self.length, 0, 0
        l1, l2 = self.dic[word1], self.dic[word2]
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")