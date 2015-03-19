# 2015-03-19 Runtime: 92 ms

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        alphanumericS = []
        for i in xrange(len(s)):
            if 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
                alphanumericS.append(s[i])
            elif 'A' <= s[i] <= 'Z':
                alphanumericS.append(chr(ord(s[i]) - ord('A') + ord('a')))
        return alphanumericS == alphanumericS[::-1]