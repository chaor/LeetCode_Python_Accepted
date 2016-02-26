# 2016-02-26  26 tests, 40 ms
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        b = c = d = e = f = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b): return True
            b, c, d, e, f = a, b, c, d, e
        return False
