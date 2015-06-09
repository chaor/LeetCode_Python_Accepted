# 2015-06-08  Runtime: 126 ms
# thanks to https://leetcode.com/discuss/10063/hash-idea-and-exception-case
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        # the key is hash('foo') + hash('bar') == hash('bar') + hash('foo')
        wordLen, wordNum, wordSet, wordHashSum = len(words[0]), len(words), set(words), sum([hash(word) for word in words])
        h = [ hash(s[i:i + wordLen]) if s[i:i + wordLen] in wordSet else 0 for i in xrange(len(s) - wordLen + 1) ]
        return [i for i in xrange(len(s) - wordLen * wordNum + 1) if sum(h[i:i + wordLen * wordNum:wordLen]) == wordHashSum]