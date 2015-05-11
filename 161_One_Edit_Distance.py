# 2015-05-11  Runtime: 69 ms
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isOneEditDistance(self, s, t):
        # make sure len(s) < len(t)
        lenS, lenT = len(s), len(t)
        if lenS > lenT: return self.isOneEditDistance(t, s)
        if lenT - lenS > 1: return False
        i = 0
        while i < lenS and s[i] == t[i]: i += 1
        if i == lenS: return lenT - lenS == 1 # append one char to t
        if lenT - lenS == 0: i += 1 # modify one char in s or in t
        # if lenT - lenS == 1, insert one char among s
        while i < lenS and s[i] == t[i + lenT - lenS]: i += 1
        return i == lenS