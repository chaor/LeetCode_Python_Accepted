# 2015-04-29 Runtime: 52 ms

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        mapping = {}
        for i in xrange(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            else:
                if mapping[s[i]] != t[i]: return False
        return len(mapping.keys()) == len(set(mapping.values()))