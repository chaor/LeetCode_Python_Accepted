# 2015-08-23   Runtime: 68 ms
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, base = 0, 1
        for ch in s[::-1]:
            res += base * ((ord(ch) - ord('A')) + 1)
            base *= 26
        return res