# 2016-03-20   134 tests, 608 ms
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 0 means the word is not reversed, 1 means the word is reversed
        words, length, result = sorted([(w, 0, i, len(w)) for i, w in enumerate(words)] +
                                       [(w[::-1], 1, i, len(w)) for i, w in enumerate(words)]), len(words) * 2, []
        for i, (word1, rev1, ind1, len1) in enumerate(words):
            for j in xrange(i + 1, length):
                word2, rev2, ind2, _ = words[j]
                if word2.startswith(word1):
                    if ind1 != ind2 and rev1 ^ rev2:
                        rest = word2[len1:]
                        if rest == rest[::-1]: result += ([ind1, ind2],) if rev2 else ([ind2, ind1],)
                else:
                    break
        return result
