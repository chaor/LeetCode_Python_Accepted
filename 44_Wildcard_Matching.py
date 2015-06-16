# 2015-06-15  Runtime: 168 ms
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        i, j, starCanMatch, lastStarPos = 0, 0, 0, -1
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
                continue
            # when meet a '*', first assume it will match 0 character
            if j < len(p) and p[j] == '*':
                lastStarPos, starCanMatch = j, i 
                j += 1
                continue
            # now p[j] is not ?, not *, can't match s[i], we can only use the last '*'
            if lastStarPos > -1:
                i = starCanMatch + 1
                starCanMatch += 1
                j = lastStarPos + 1
                continue
            return False
        while j < len(p) and p[j] == '*': j += 1
        return j == len(p)