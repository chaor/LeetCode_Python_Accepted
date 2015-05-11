# 2015-05-11  Runtime: 1379 ms
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in xrange(len(s)):
            # assume center is s[i], then expand
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]: L, R = L - 1, R + 1
            len1 = R - L - 1
            # assume center is between s[i] and s[i+1], then expand
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]: L, R = L - 1, R + 1
            len2 = R - L - 1
            length = len1 if len1 > len2 else len2
            if length > end - start:
                start, end = i - (length - 1) / 2, i + length / 2
        return s[start:end + 1]