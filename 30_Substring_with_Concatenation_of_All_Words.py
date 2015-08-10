# 2015-08-09  Runtime: 172 ms
# thanks to https://leetcode.com/discuss/10063/hash-idea-and-exception-case
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        # we can use sorted(words), but sorted(Hash values) is much faster than sorted(words)
        wordLen, wordNum, Set, sortHash = len(words[0]), len(words), set(words), sorted([hash(word) for word in words])
        h = [ hash(s[i:i + wordLen]) if s[i:i + wordLen] in Set else 0 for i in xrange(len(s) - wordLen + 1) ]
        return [i for i in xrange(len(s) - wordLen * wordNum + 1) if sorted(h[i : i + wordLen * wordNum : wordLen]) == sortHash]