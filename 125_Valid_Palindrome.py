# 2015-09-29  Runtime: 76 ms
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [ch.lower() for ch in s if ch.isalnum()]
        return s == s[::-1]
        