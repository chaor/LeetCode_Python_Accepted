# 2015-12-24  15 tests, 248 ms
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        numPool = []
        for i in range(len(low), len(high) + 1):
            numPool += self.nDigit(i)
        return bisect.bisect_right(numPool, int(high)) - bisect.bisect_left(numPool, int(low))

    # Find all strobogrammatic numbers that are of length = n
    def nDigit(self, n):
        res = ['0', '1', '8'] if n % 2 else ['']
        while n >= 2:
            n -= 2
            if n < 2:
                res = [a + s + b for a, b in ('11', '69', '88', '96') for s in res]
            else:
                res = [a + s + b for a, b in ('00', '11', '69', '88', '96') for s in res]
        return [int(i) for i in res]
