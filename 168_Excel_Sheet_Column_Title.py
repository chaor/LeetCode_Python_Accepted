# 2014-08-23  Runtime: 40 ms
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n > 0:
            res.append(chr((n - 1) % 26 + ord('A')))
            n = (n - 1) / 26
        return ''.join(res[::-1])