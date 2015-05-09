# 2015-05-09  Runtime: 85 ms
class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        i, n = 0, len(s)
        while i < n and s[i] == ' ': i += 1
        if i < n and s[i] in ('+', '-'): i += 1
        isNumeric = False
        while i < n and '0' <= s[i] <= '9': i, isNumeric = i + 1, True
        if i < n and s[i] == '.':
            i += 1
            while i < n and '0' <= s[i] <= '9': i, isNumeric = i + 1, True
        if i < n and s[i] == 'e':
            i += 1
            if i < n and s[i] in ('+', '-'): i += 1
            # make sure there's at least on digit after 'e'
            if i == n or not '0' <= s[i] <= '9': return False
            while i < n and '0' <= s[i] <= '9': i += 1
        while i < n and s[i] == ' ': i += 1
        return isNumeric and i == n