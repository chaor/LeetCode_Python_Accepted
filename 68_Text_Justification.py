# 2015-07-09  Runtime: 44 ms
class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        # thanks to https://leetcode.com/discuss/13610/share-my-concise-c-solution-less-than-20-lines
        res = []
        start, k, charCount = 0, None, None
        while start < len(words):
            k, charCount = 0, 0
            while start + k < len(words) and charCount + len(words[start + k]) + k <= maxWidth:
                charCount += len(words[start + k])
                k += 1
            oneLine = words[start]
            for j in xrange(k - 1):
                if start + k >= len(words):
                    oneLine += ' '
                else:
                    oneLine += ' ' * ((maxWidth - charCount) / (k - 1) + (j < (maxWidth - charCount) % (k - 1)))
                oneLine += words[start + j + 1]
            oneLine += ' ' * (maxWidth - len(oneLine))
            res.append(oneLine)
            start += k
        return res 