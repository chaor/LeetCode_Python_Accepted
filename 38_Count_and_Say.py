# 2015-06-14  Runtime: 56 ms
class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n == 1: return '1'
        if n == 2: return '11'
        s, L = '11', []
        for i in xrange(3, n + 1):
            currChar, count = s[0], 1
            for j in xrange(1, len(s)):
                if s[j] != s[j-1]:
                    L.extend([str(count), currChar])
                    count, currChar = 1, s[j]
                else:
                    count += 1
            L.extend([str(count), currChar])
            s, L = ''.join(L), []
        return s