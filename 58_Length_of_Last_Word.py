# 2015-06-18   Runtime: 52 ms
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        i, L = 0, 0
        while i < len(s):
            if s[i] != ' ':
                L += 1
                i += 1
            else:
                i += 1
                if i < len(s) and s[i] != ' ': L = 0
        return L