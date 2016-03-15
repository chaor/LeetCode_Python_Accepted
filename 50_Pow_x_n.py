# 2016-03-15  300 tests, 40 ms
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0: x, n = 1.0 / x, -n
        result, weight = 1, x
        while n: # consider binary
            if n & 1: result *= weight
            weight **= 2 # square
            n >>= 1
        return result
